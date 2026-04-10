import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import research_tools

load_dotenv()
CLIENT = OpenAI()

TOOL_MAPPING = {
    "tavily_search_tool": research_tools.tavily_search_tool,
    "arxiv_search_tool": research_tools.arxiv_search_tool,
}


# ── Exercise 1 ────────────────────────────────────────────────────────────────

def generate_research_report_with_tools(prompt: str, model: str = "gpt-4o") -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a research assistant that can search the web and arXiv to write detailed, "
                "accurate, and properly sourced research reports.\n\n"
                "🔍 Use tools when appropriate.\n"
                "📚 Cite sources whenever relevant.\n"
                "🌐 Include full URLs where possible.\n"
                "✍️ Use an academic tone with clearly labeled sections.\n"
                "🚫 Do not include placeholder text."
            )
        },
        {"role": "user", "content": prompt}
    ]
    tools = [research_tools.arxiv_tool_def, research_tools.tavily_tool_def]
    max_turns = 10
    final_text = ""

    for _ in range(max_turns):
        response = CLIENT.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=0,
        )
        msg = response.choices[0].message
        messages.append(msg)

        if not msg.tool_calls:
            final_text = msg.content
            print("✅ Final answer:")
            print(final_text)
            break

        for call in msg.tool_calls:
            tool_name = call.function.name
            args = json.loads(call.function.arguments)
            print(f"🛠️ {tool_name}({args})")
            try:
                tool_func = TOOL_MAPPING[tool_name]
                result = tool_func(**args)
            except Exception as e:
                result = {"error": str(e)}

            new_msg = {
                "role": "tool",
                "tool_call_id": call.id,
                "name": tool_name,
                "content": json.dumps(result)
            }
            messages.append(new_msg)

    return final_text


# ── Exercise 2 ────────────────────────────────────────────────────────────────

def reflection_and_rewrite(report, model: str = "gpt-4o-mini", temperature: float = 0.3) -> dict:
    report = research_tools.parse_input(report)

    user_prompt = f"""You are given the following research report:

{report}

Please analyze the report and return ONLY valid JSON with exactly this structure, no extra commentary:
{{
    "reflection": "A structured reflection that MUST explicitly cover all four of these labeled sections: Strengths, Limitations, Suggestions, and Opportunities.",
    "revised_report": "An improved version of the report with better clarity and academic tone."
}}

The 'reflection' value MUST contain all four headings: Strengths, Limitations, Suggestions, Opportunities."""

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an academic reviewer and editor."},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature
    )

    llm_output = response.choices[0].message.content.strip()

    try:
        data = json.loads(llm_output)
    except json.JSONDecodeError:
        raise Exception("The output of the LLM was not valid JSON. Adjust your prompt.")

    return {
        "reflection": str(data.get("reflection", "")).strip(),
        "revised_report": str(data.get("revised_report", "")).strip(),
    }


# ── Exercise 3 ────────────────────────────────────────────────────────────────

def convert_report_to_html(report, model: str = "gpt-4o", temperature: float = 0.5) -> str:
    report = research_tools.parse_input(report)
    system_prompt = "You convert plaintext reports into full clean HTML documents."

    user_prompt = f"""Convert the following research report into a well-structured HTML document.

Requirements:
- Use appropriate HTML tags: headings (<h1>, <h2>, <h3>), paragraphs (<p>), lists (<ul>, <li>)
- Make all URLs into clickable <a href="..."> links
- Preserve the citation style from the original
- Return ONLY valid HTML, no extra commentary or markdown

Report:
{report}"""

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature
    )

    return response.choices[0].message.content.strip()


# ── End-to-end pipeline ───────────────────────────────────────────────────────

if __name__ == "__main__":
    prompt_ = "Radio observations of recurrent novae"

    print("=== Step 1: Research Report ===")
    preliminary_report = generate_research_report_with_tools(prompt_)

    print("\n=== Step 2: Reflection & Rewrite ===")
    reflection_result = reflection_and_rewrite(preliminary_report)
    print(reflection_result["reflection"])

    print("\n=== Step 3: Convert to HTML ===")
    html = convert_report_to_html(reflection_result["revised_report"])
    print(html[:500], "\n... [truncated]")
