import arxiv
from tavily import TavilyClient
import os

# ── Tool definitions (passed to OpenAI tool-calling) ──────────────────────────

arxiv_tool_def = {
    "type": "function",
    "function": {
        "name": "arxiv_search_tool",
        "description": "Search academic papers on arXiv.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
                "max_results": {"type": "integer", "default": 5}
            },
            "required": ["query"]
        }
    }
}

tavily_tool_def = {
    "type": "function",
    "function": {
        "name": "tavily_search_tool",
        "description": "Search the web using Tavily.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
                "max_results": {"type": "integer", "default": 5},
                "include_images": {"type": "boolean", "default": False}
            },
            "required": ["query"]
        }
    }
}

# ── Tool implementations ───────────────────────────────────────────────────────

def arxiv_search_tool(query: str, max_results: int = 5) -> list:
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=max_results)
    results = []
    for paper in client.results(search):
        results.append({
            "title": paper.title,
            "authors": [a.name for a in paper.authors],
            "published": str(paper.published.date()),
            "url": paper.entry_id,
            "summary": paper.summary,
            "link_pdf": paper.pdf_url
        })
    return results


def tavily_search_tool(query: str, max_results: int = 5, include_images: bool = False) -> list:
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    response = client.search(query=query, max_results=max_results, include_images=include_images)
    return [
        {"title": r["title"], "content": r["content"], "url": r["url"]}
        for r in response.get("results", [])
    ]


def parse_input(report) -> str:
    """Accepts raw text or a messages list; returns plain text."""
    if isinstance(report, list):
        for msg in reversed(report):
            role = msg.get("role") if isinstance(msg, dict) else getattr(msg, "role", None)
            content = msg.get("content") if isinstance(msg, dict) else getattr(msg, "content", None)
            if role == "assistant" and content:
                return content
        return ""
    return report
