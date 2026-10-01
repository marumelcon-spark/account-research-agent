from urllib.parse import urlparse
import re
import os
from tavily import TavilyClient
import csv
import difflib
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
CRM_FILE = DATA_DIR / "crm_accounts.csv"
FIRMO_FILE = DATA_DIR / "firmographics.csv"


def _load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def _norm(text):
    """Lowercase and drop punctuation: 'Harborline Freight Co.' -> 'harborline freight co'."""
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", text.lower()).split())


def _find(rows, account_name):
    """Shared matching: ignores case and punctuation, and matches aliases in parentheses."""
    query = _norm(account_name)
    for row in rows:
        name = row["account_name"]
        aliases = [_norm(a) for a in name.replace(")", "").split("(")]
        if query == _norm(name) or query in aliases:
            return row
    return None


def _not_found(rows, account_name, source):
    names = [r["account_name"] for r in rows]
    return {
        "found": False,
        "source": source,
        "message": f"No record matches '{account_name}' in {source}.",
        "similar_names": difflib.get_close_matches(account_name, names, n=3, cutoff=0.5),
    }


def _clean(row):
    record = {k: (v if v != "" else None) for k, v in row.items()}
    missing = [k for k, v in record.items() if v is None]
    return record, missing


def crm_lookup(account_name: str) -> dict:
    rows = _load(CRM_FILE)
    row = _find(rows, account_name)
    if row is None:
        return _not_found(rows, account_name, "crm_accounts.csv")
    record, missing = _clean(row)
    return {
        "found": True,
        "source": f"crm_accounts.csv, {record['account_id']}",
        "record": record,
        "missing_fields": missing,
    }


def firmographic_lookup(account_name: str) -> dict:
    rows = _load(FIRMO_FILE)
    row = _find(rows, account_name)
    if row is None:
        return _not_found(rows, account_name, "firmographics.csv")
    record, missing = _clean(row)
    return {
        "found": True,
        "source": f"firmographics.csv ({record['data_source']})",
        "record": record,
        "missing_fields": missing,
    }


CRM_LOOKUP_TOOL = {
    "name": "crm_lookup",
    "description": (
        "Look up a single account in the internal CRM by company name. "
        "Returns the account's deal stage, product interest, ARR in USD "
        "(null = not yet a customer), renewal/close date, account owner "
        "(null = unassigned), champion's job title (null = none identified), "
        "last logged activity, and the rep's free-text notes, which may be "
        "incomplete or contradictory. Also returns 'missing_fields' listing "
        "every blank field. If the account is not found, returns similar names; "
        "do not assume a similar name is the same company without saying so."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "account_name": {"type": "string", "description": "Company name, e.g. 'Petco' or 'Instacart'."}
        },
        "required": ["account_name"],
    },
}

FIRMOGRAPHIC_LOOKUP_TOOL = {
    "name": "firmographic_lookup",
    "description": (
        "Look up third-party enrichment data about a company (like ZoomInfo): "
        "headquarters, employee and revenue bands, ownership (public, private, "
        "PE-owned, nonprofit), identity/SSO provider, and other detected technologies. "
        "Use it for company context and tech-stack fit, not deal status. "
        "Null fields are unknown, not 'none'. Returns 'missing_fields' listing blanks. "
        "If the company is not found, say enrichment data is unavailable."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "account_name": {"type": "string", "description": "Company name, e.g. 'Zillow'."}
        },
        "required": ["account_name"],
    },
}


SOCIAL = ("linkedin.com", "x.com", "twitter.com", "facebook.com", "instagram.com",
          "youtube.com", "tiktok.com", "reddit.com", "quora.com", "medium.com", "substack.com")
MAJOR_NEWS = ("wsj.com", "reuters.com", "bloomberg.com", "cnbc.com", "nytimes.com", "ft.com",
              "apnews.com", "latimes.com", "washingtonpost.com", "forbes.com", "fortune.com",
              "time.com", "axios.com", "techcrunch.com", "theverge.com", "geekwire.com",
              "businessinsider.com", "finance.yahoo.com", "prnewswire.com", "businesswire.com",
              "globenewswire.com", "sec.gov")
AGGREGATOR_HINTS = ("layoff", "interviewpal", "zoominfo", "rocketreach", "crunchbase",
                    "glassdoor", "wiza", "signalhire", "bizofco", "opencorporates")
LEGAL_HINTS = ("law", "legal", "attorney", "borrelli")


def _domain_match(host, domains):
    return any(host == d or host.endswith("." + d) for d in domains)


def _source_type(url, query):
    """Label a web result by where it comes from, before the model sees it."""
    parsed = urlparse(url or "")
    host = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.lower()
    company = query.split()[0].lower() if query else ""
    if _domain_match(host, SOCIAL):
        return "unverified: social/video"
    if "forum" in host or "/forum" in path or "/t/" in path:
        return "unverified: forum"
    if _domain_match(host, MAJOR_NEWS):
        return "major_news"
    if company and company in host:
        return "company_site (name match: confirm same company)"
    if any(h in host for h in AGGREGATOR_HINTS):
        return "unverified: data aggregator"
    if any(h in host for h in LEGAL_HINTS):
        return "unverified: law-firm marketing"
    if host.startswith("blog.") or "/blog" in path:
        return "unverified: blog"
    return "other"

def web_search(query: str) -> dict:
    """Search the live web (past year) and return the top results with URLs."""
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        return {"found": False, "source": "web_search", "error": "TAVILY_API_KEY is not set."}
    try:
        client = TavilyClient(api_key=api_key)
        response = client.search(query, max_results=5, time_range="year")
    except Exception as e:
        return {"found": False, "source": "web_search", "error": f"Search failed: {e}"}

    results = [
        {
            "title": r.get("title"),
            "url": r.get("url"),
            "snippet": (r.get("content") or "")[:500],
            "published_date": r.get("published_date"),
            "source_type": _source_type(r.get("url"), query),
        }
        for r in response.get("results", [])
    ]
    if not results:
        return {"found": False, "source": "web_search", "query": query,
                "message": "No web results found."}
    return {"found": True, "source": "web_search (Tavily)", "query": query, "results": results}


WEB_SEARCH_TOOL = {
    "name": "web_search",
    "description": (
        "Search the public web for recent news and events about a company "
        "(past 12 months): leadership changes, layoffs, funding, acquisitions, "
        "security incidents, earnings, strategy. Write a specific query such as "
        "'Petco layoffs 2026' or 'Wayfair CISO'. Returns up to 5 results with "
        "title, URL, snippet and date. Results may be about a DIFFERENT company "
        "with a similar name: only use results clearly about the account, and "
        "cite the URL for every fact taken from them. If nothing relevant comes "
        "back, say so; do not fill the gap from general knowledge."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "A specific search query including the company name."}
        },
        "required": ["query"],
    },
}

if __name__ == "__main__":
    print(json.dumps(web_search("Wayfair news 2026"), indent=2))