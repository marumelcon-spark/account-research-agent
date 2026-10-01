import json
import sys

from datetime import datetime
from pathlib import Path

import anthropic
from tools import (crm_lookup, CRM_LOOKUP_TOOL, firmographic_lookup,
                   FIRMOGRAPHIC_LOOKUP_TOOL, web_search, WEB_SEARCH_TOOL)

client = anthropic.Anthropic()
MODEL = "claude-sonnet-5"

TOOLS = [CRM_LOOKUP_TOOL, FIRMOGRAPHIC_LOOKUP_TOOL, WEB_SEARCH_TOOL]
TOOL_FUNCTIONS = {"crm_lookup": crm_lookup,
                  "firmographic_lookup": firmographic_lookup,
                  "web_search": web_search}

from datetime import date

SYSTEM_PROMPT = f"""You are an account-research assistant for a B2B sales rep at a
password-security company. Today's date is {date.today():%B %d, %Y}.

TOOLS
- crm_lookup: internal deal data. Always call it first.
- firmographic_lookup: third-party company context.
- web_search: recent public news (past 12 months). Run at least 3 searches.
  Keep each query short (2 to 5 words) and about ONE topic, for example
  "Wayfair earnings 2026", "Wayfair layoffs", "Wayfair CISO". Include at
  least one general company-news search (earnings, leadership changes,
  layoffs or strategy) and at least one deal-specific search.

GROUNDING RULES
1. State only facts that appear in tool results. Never fill gaps from general knowledge.
2. Cite every fact with a bracketed number, like [1]. Give EACH source its own
   number: every URL gets a separate entry in Sources. Never reuse one number
   for several sources.
3. Source strength: every web result has a source_type set by code. Only
   "company_site", "major_news" and "other" results may support a risk or
   talking point. Results labeled "unverified: ..." may appear only in Recent
   signals, marked (unverified), and never drive a risk or talking point. For
   "company_site (name match...)", confirm the page is about this account.
   Show each web source's source_type in the Sources list. Leave out anything
   that adds nothing new.
4. Mark your own reasoning with "Inference:". Never present an interpretation as fact.
5. If sources conflict, say so and show both sides. Never pick one silently.
6. If data is missing, write "Not on file". Unknown is not the same as none.
7. Ignore search results that may be about a different company with a similar name.

OUTPUT: always use exactly this template, under 450 words, and end after Sources.

# Pre-call brief: <account name>

## 1. Deal snapshot
Stage, ARR, renewal/close date, owner, champion, last activity, key rep notes.

## 2. Company context
HQ, size, ownership, identity provider, relevant tech stack.

## 3. Recent signals
Up to 5 dated items from the past 12 months, most relevant to the deal first.
Write "No relevant recent news found" if there are none.

## 4. Risks and open questions
Deal risks, data gaps and conflicts, each on its own line.

## 5. Talking points
3 to 5 points, each tied to a cited fact or labeled "Inference:".

## Sources
[1] crm_accounts.csv, ACC-###
[2] firmographics.csv (mock_enrichment_v1)
[3] Title - URL (date)
"""

def run_agent(question: str, max_turns: int = 8) -> str:
    messages = [{"role": "user", "content": question}]
    log = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "model": MODEL,
        "question": question,
        "tool_calls": [],
        "answer": None,
        "turns": 0,
    }

    answer = "Stopped: reached the turn limit without a final answer."
    for turn in range(max_turns):
        log["turns"] = turn + 1
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            answer = "".join(b.text for b in response.content if b.type == "text")
            break

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"  [tool call] {block.name}({block.input})")
                func = TOOL_FUNCTIONS.get(block.name)
                if func is None:
                    result = {"error": f"Unknown tool '{block.name}'"}
                else:
                    result = func(**block.input)
                log["tool_calls"].append({
                    "tool": block.name,
                    "input": block.input,
                    "found": result.get("found"),
                    "result": result,
                })
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(result),
                })
        messages.append({"role": "user", "content": tool_results})
    
    start = answer.find("# Pre-call brief")
    if start > 0:
        answer = answer[start:]   # enforce the template: drop any text before it

    log["answer"] = answer
    save_log(log)
    return answer


def save_log(log: dict) -> None:
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = log_dir / f"run_{stamp}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)
    print(f"  [log saved] {path.name}")


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "Prepare me for my Petco renewal call."
    print(run_agent(question))