# Pre-call brief: Zillow

## 1. Deal snapshot
- Stage: Expansion - Discovery [1]
- Product interest: Secrets Automation [1]
- ARR: $140,000 (existing Enterprise customer) [1]
- Close/renewal date: 2026-12-01 [1]
- Owner: Alex Kim [1]
- Champion: Director of DevOps [1]
- Last activity: 2026-09-11, workshop on secrets management for DevOps [1]
- Rep notes: Evaluating us vs. HashiCorp Vault for secrets management; DevOps team prefers our UX, but security architecture team prefers Vault [1]

## 2. Company context
- HQ: Seattle, WA [2]
- Size: 5,000–10,000 employees (CRM lists 6,000) [1][2]; Revenue band $1B–5B [2]
- Ownership: Public [2]
- Identity provider: Okta [2]
- Tech stack: AWS, Kubernetes, Terraform, HashiCorp Vault (pilot) [2] — confirms rep notes that Vault is already in use, likely the internal incumbent security architecture is pushing for

## 3. Recent signals
1. Q2 2026 earnings: revenue $772M (+18% YoY); mortgage revenue up 75% to $84M; net loss of $4M despite segment growth — "Housing Super App" strategy highlighted [3].
2. Zillow reaffirmed FY2026 financial outlook and highlighted an "AI-native housing platform strategy" at its AI Summit for Investors, March 24, 2026 [4].
3. Stock-analysis commentary notes Zillow "Reshuffles Leadership with New Executive Appointments" alongside a Q2 quarterly loss — headline only, no detail on which roles changed [5].
4. Analyst commentary flags competitive pressure from CoStar in residential listings and antitrust/legal scrutiny tied to a Redfin-related securities class action [5].
5. (unverified) A security-blog piece references a past AI failure at Zillow as a cautionary case study — not confirmed as company-official, include only as unverified context [6].

## 4. Risks and open questions
- Internal split between DevOps (favors us) and security architecture (favors Vault) is the central deal risk [1].
- No CISO or security-leadership contact identified in search results; unclear who owns final security tooling decision — gap to fill before call.
- Leadership reshuffle mentioned in analyst commentary [5] is vague; unknown if it affects security/DevOps org — worth asking champion directly.
- Renewal/close date (2026-12-01) is ~2 months out; discovery stage timeline is tight given competing vendor evaluation.
- Company is navigating legal/antitrust scrutiny [5] — could affect budget scrutiny or procurement pace; not confirmed to impact this deal.

## 5. Talking points
1. Zillow already runs Vault in pilot alongside Terraform/Kubernetes on AWS [2] — position our tool as complementary/migration-friendly rather than rip-and-replace, addressing security team's Vault familiarity.
2. DevOps has already engaged in a hands-on workshop (9/11) [1] — build on that momentum by proposing a joint session with the security architecture team to address their concerns directly.
3. Inference: Given Zillow's "AI-native platform" and Super App strategy emphasis [3][4], frame secrets automation as enabling secure scaling of their expanding AI/infrastructure footprint.
4. Ask champion about the leadership reshuffle mentioned externally [5] to see if it affects the security architecture stakeholder or budget owner.
5. With close date 12/1, propose a clear evaluation timeline now to avoid losing momentum to Vault.

## Sources
[1] crm_accounts.csv, ACC-007
[2] firmographics.csv (mock_enrichment_v1)
[3] "Zillow says its 'Housing Super App' strategy is working" - https://www.housingwire.com/articles/zillow-q2-2026-earnings (other)
[4] "Zillow Group to highlight AI-native housing platform strategy at AI Summit for Investors" - https://zillowgroup.mediaroom.com/2026-03-24-Zillow-Group-to-highlight-AI-native-housing-platform-strategy-at-AI-Summit-for-Investors (company_site, name match confirmed – Zillow Group official newsroom)
[5] "Zillow Group (NasdaqGS:ZG) Stock Forecast & Analyst Predictions" - https://simplywall.st/stocks/us/real-estate-management-and-development/nasdaq-zg/zillow-group/future (other)
[6] "5 Real AI Failures That Every Organization Can Learn From" - https://www.klogixsecurity.com/blog/5-real-ai-failures-that-every-organization-can-learn-from (unverified: blog)