"""Build a side-by-side review page: each brief next to its scores.

Usage (from the project folder):  python evaluation\make_review.py baseline
Compare two runs:                 python evaluation\make_review.py after_fix baseline
Reads briefs\<label>\*.md and evaluation\scores_<label>.csv,
writes evaluation\review_<label>.html. Double-click the HTML to open it.
"""
import csv
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
label = sys.argv[1] if len(sys.argv) > 1 else "baseline"
compare = sys.argv[2] if len(sys.argv) > 2 else None
CRITERIA = ["groundedness", "completeness", "actionability", "signal_quality", "failure_handling"]

def load_scores(lab):
    out = {}
    path = ROOT / "evaluation" / f"scores_{lab}.csv"
    if lab and path.exists():
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                out[row["account"].replace(" ", "_").replace(".", "")] = row
    return out


scores = load_scores(label)
before = load_scores(compare) if compare else {}


def avg(c, table=None):
    table = scores if table is None else table
    vals = [int(r[c]) for r in table.values() if r.get(c)]
    return f"{sum(vals) / len(vals):.1f}" if vals else "-"


def cell(v, old=None):
    if not v:
        return '<td class="na">n/a</td>'
    arrow = ""
    if old and old != v:
        arrow = f' <span class="was">(was {old})</span>'
    return f'<td class="s{v}">{v}{arrow}</td>'


parts = []
summary_rows = "".join(
    f"<tr><th>{html.escape(r['account'])}</th>"
    + "".join(cell(r.get(c, ""), before.get(k, {}).get(c)) for c in CRITERIA) + "</tr>"
    for k, r in scores.items()
)
summary_rows += "<tr class='avg'><th>Average</th>" + "".join(
    f"<td>{avg(c)}" + (f' <span class="was">(was {avg(c, before)})</span>' if before else "") + "</td>"
    for c in CRITERIA) + "</tr>"
head = "".join(f"<th>{c.replace('_', ' ')}</th>" for c in CRITERIA)

for brief_path in sorted((ROOT / "briefs" / label).glob("*.md")):
    key = brief_path.stem
    row = scores.get(key, {})
    brief = html.escape(brief_path.read_text(encoding="utf-8"))
    score_list = "".join(
        f"<tr><th>{c.replace('_', ' ')}</th>{cell(row.get(c, ''), before.get(key, {}).get(c))}</tr>" for c in CRITERIA
    )
    notes = html.escape(row.get("notes", "No scores yet."))
    parts.append(f"""
<section>
  <h2>{html.escape(row.get('account', key))}</h2>
  <div class="pair">
    <pre class="brief">{brief}</pre>
    <aside>
      <table class="scores">{score_list}</table>
      <p class="notes">{notes}</p>
    </aside>
  </div>
</section>""")

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Brief review: {label}</title>
<style>
  body {{ font-family: Segoe UI, Arial, sans-serif; margin: 0; padding: 24px; background: #f6f6f4; color: #222; }}
  h1 {{ margin-top: 0; }}
  table {{ border-collapse: collapse; }}
  th, td {{ padding: 6px 10px; border-bottom: 1px solid #ddd; text-align: left; }}
  td {{ text-align: center; font-weight: 600; }}
  .summary {{ background: #fff; margin-bottom: 32px; }}
  .avg th, .avg td {{ border-top: 2px solid #999; }}
  section {{ background: #fff; border-radius: 8px; padding: 16px 20px; margin-bottom: 24px; }}
  .pair {{ display: grid; grid-template-columns: minmax(0, 2fr) minmax(260px, 1fr); gap: 24px; }}
  .brief {{ white-space: pre-wrap; font-family: Consolas, monospace; font-size: 13px; line-height: 1.45;
           background: #fafafa; padding: 12px; border-radius: 6px; max-height: 80vh; overflow: auto; margin: 0; }}
  aside {{ position: sticky; top: 16px; align-self: start; }}
  .notes {{ font-size: 14px; line-height: 1.5; }}
  .s5 {{ background: #d7eed8; }} .s4 {{ background: #e8f3d6; }} .s3 {{ background: #fbeec8; }}
  .s2 {{ background: #f8d9c4; }} .s1 {{ background: #f3c2c2; }} .na {{ color: #888; font-weight: 400; }}
  .was {{ font-weight: 400; font-size: 12px; color: #555; }}
  @media (max-width: 800px) {{ .pair {{ grid-template-columns: 1fr; }} aside {{ position: static; }} }}
</style></head><body>
<h1>Brief review: {label}{f" (compared with {compare})" if compare else ""}</h1>
<p>Scores 1-5 per <code>evaluation/RUBRIC.md</code>. Brief on the left, scores and reasons on the right.</p>
<table class="summary"><tr><th>Account</th>{head}</tr>{summary_rows}</table>
{''.join(parts)}
</body></html>"""

out = ROOT / "evaluation" / f"review_{label}.html"
out.write_text(page, encoding="utf-8")
print(f"Review page written: {out}")
