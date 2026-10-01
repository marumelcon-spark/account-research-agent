# Evaluation Rubric

Each pre-call brief is scored 1-5 on five criteria. Anchors were defined before scoring so that
before/after comparisons use the same bar. Scores are drafted by Claude and reviewed by a human
(Mariana), whose sales judgment is final, especially on actionability.

## 1. Groundedness: is every claim traceable to a real source?
| Score | Anchor |
|---|---|
| 5 | Every fact cites a numbered source; no weak source shapes a risk or talking point |
| 4 | All facts sourced; one minor citation slip (non-numbered or vague date) |
| 3 | A weak/unverified source drives a risk or talking point, or one claim is misattributed |
| 2 | Several claims unsupported or misattributed |
| 1 | Fabricated facts |

## 2. Completeness: are all sections filled with useful content, not filler?
| Score | Anchor |
|---|---|
| 5 | All six sections populated with relevant, non-repetitive content |
| 4 | All sections present; one thin section or some filler lines |
| 3 | One section missing useful content that the tools could have provided |
| 2 | Several sections thin or missing |
| 1 | Template not followed |
An empty section that correctly says nothing was found (e.g. no news for a fictional company) is not penalized; filler lines are.

## 3. Actionability: would a rep actually say or do this on the call?
Each talking point is checked for: specific to this account, tied to a fact or a labeled inference,
usable as a question, point or confirmation in the conversation.
| Score | Anchor |
|---|---|
| 5 | Every talking point specific, grounded and usable as-is |
| 4 | Mostly strong; one generic or awkward point |
| 3 | Mix of useful and generic points, or one based on a weak source |
| 2 | Mostly generic advice ("highlight ROI") |
| 1 | Nothing a rep could use |

## 4. Signal quality: did the agent surface something non-obvious and relevant?
| Score | Anchor |
|---|---|
| 5 | Found a non-obvious signal that changes the call strategy (e.g. competitor already in pilot, security leader left) |
| 4 | Relevant, dated, recent signals from credible sources |
| 3 | Generic or loosely relevant news only |
| 2 | Missed obvious available news (e.g. no company news for a large public company) |
| 1 | Irrelevant or wrong-company signals |
Not scored when there is genuinely nothing to find (fictional company).

## 5. Failure handling: when data is missing, wrong or conflicting, does the brief say so?
Checks: missing CRM fields ("Not on file"), conflicting data (both sides shown), empty or irrelevant
search results (said plainly; look-alike companies rejected), unverifiable claims (flagged to confirm).
| Score | Anchor |
|---|---|
| 5 | Every gap and conflict named and turned into something to verify on the call |
| 4 | Gaps handled honestly with minor slips |
| 3 | Some gaps named, others glossed over |
| 2 | A gap filled with a plausible-sounding guess |
| 1 | Invented facts presented as real |

## Review log
- Baseline (2026-09-30): scores drafted by Claude, reviewed side by side by Mariana in `review_baseline.html` and confirmed. Clarified the completeness rule for empty sections after her question about Harborline.

## Test set
| Account | What it tests |
|---|---|
| Wayfair | Rich data and lots of news |
| JetBlue | Conflicting CRM notes |
| Zillow | Competitive deal (vs. HashiCorp Vault already in pilot) |
| Rivian | Sparse CRM record |
| Harborline Freight Co. | Fictional company: web search must find nothing and reject look-alikes |
