# Simple Research Tool with Reflection

A research pipeline using OpenAI tool-calling to search arXiv and the web,
reflect on results, and convert reports to HTML.

## Pipeline
1. **generate_research_report_with_tools** — searches arXiv + Tavily, writes a sourced report
2. **reflection_and_rewrite** — reflects on the report (Strengths, Limitations, Suggestions, Opportunities) and rewrites it
3. **convert_report_to_html** — converts the final report to a clean HTML document

## Setup
1. Clone the repo
```bash
   git clone https://github.com/devras-ai-architect/simple-research-tool.git
   cd simple-research-tool
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
3. Create a `.env` file with your API keys
