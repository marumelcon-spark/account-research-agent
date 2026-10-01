"""Run the agent on the 5 evaluation accounts and save each brief for scoring."""
import sys
from pathlib import Path

from agent import run_agent

ACCOUNTS = [
    "Wayfair",           # rich data + lots of news
    "JetBlue",           # conflicting CRM notes
    "Zillow",            # competitive deal (vs. HashiCorp Vault)
    "Rivian",            # sparse CRM record
    "Harborline Freight Co.",  # fictional: web search should find nothing
]

label = sys.argv[1] if len(sys.argv) > 1 else "baseline"
out_dir = Path(__file__).parent / "briefs" / label
out_dir.mkdir(parents=True, exist_ok=True)

for name in ACCOUNTS:
    print(f"\n===== {name} =====")
    brief = run_agent(f"Prepare me for a call with {name}")
    safe = name.replace(" ", "_").replace(".", "")
    (out_dir / f"{safe}.md").write_text(brief, encoding="utf-8")
    print(f"  [brief saved] briefs/{label}/{safe}.md")

print(f"\nDone. {len(ACCOUNTS)} briefs saved in briefs/{label}/")