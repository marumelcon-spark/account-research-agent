# Pre-call brief: Zillow

## 1. Deal snapshot
- Stage: Expansion - Discovery [1]
- Product interest: Secrets Automation [1]
- ARR: $140,000 [1]
- Close/renewal date: 2026-12-01 [1]
- Owner: Alex Kim [1]
- Champion: Director of DevOps [1]
- Last activity: 2026-09-11, workshop on secrets management for DevOps [1]
- Rep notes: Existing Enterprise customer; actively evaluating us vs. HashiCorp Vault for secrets management. DevOps prefers our UX, but the security architecture team prefers Vault [1].

## 2. Company context
- HQ: Seattle, WA [2]
- Size: 5,000–10,000 employees; revenue band $1B–5B [2]
- Ownership: Public [2]
- Identity provider: Okta [2]
- Tech stack: AWS, Kubernetes, Terraform, HashiCorp Vault (pilot) [2] — consistent with CRM notes that Vault is a live competitor already in-house.

## 3. Recent signals
1. Q2 2026 earnings (reported Aug 5, 2026): revenue $772M, up 18% YoY; GAAP EPS swung to a $0.02 loss vs. $0.01 income a year earlier; adjusted EBITDA margin narrowed [3][4].
2. Company describes its "Housing Super App" strategy as working, with growth across for-sale, rentals, and mortgage segments [5].
3. Q1 2026 results showed upward financial restatement (adjusted net income revised from $129M to $145M) [6].
4. (Unverified) A LinkedIn post referenced Zillow hiring a Lead Incident Response Analyst for its security team, suggesting active security org buildout — source is a personal social post, not confirmed [7].
5. (Unverified) An Okta customer blog mentions Zillow's AI initiatives tied to identity, but does not confirm a named CISO or specific security award for Zillow [8].

## 4. Risks and open questions
- Core competitive risk: internal split between DevOps (favors us) and security architecture team (favors Vault) — deal could stall without security buy-in [1].
- Vault is already piloted in their stack per firmographics, raising switching-cost/inertia risk [2].
- No named CISO or security leader identified in public sources — unclear who the ultimate economic buyer/blocker is on the security side.
- Narrowing margins and a swing to GAAP net loss in Q2 2026 [4] could invite budget scrutiny on new security tooling — Inference: worth probing budget appetite given cost-conscious signals.
- Champion title (Director of DevOps) is a mid-level sponsor — confirm executive sponsorship exists for a $140K+ expansion.

## 5. Talking points
- Acknowledge Zillow's growth story (18% YoY revenue) [3] while noting margin pressure [4] — Inference: efficiency and consolidation messaging may resonate.
- Directly address the DevOps-vs-security tension: come with a security-architecture-focused ROI/compliance narrative to counter Vault preference [1].
- Ask who owns final sign-off given no named CISO found — confirm decision-making chain.
- Leverage existing Okta identity provider [2] for integration/SSO talking points.
- Reference the Sept 11 workshop outcome to continue the DevOps momentum into a security-team-focused follow-up [1].

## Sources
[1] crm_accounts.csv, ACC-007
[2] firmographics.csv (mock_enrichment_v1)
[3] Zillow Q2 2026 Earnings: Revenue Rises 18% as Margins Narrow - https://www.tradingkey.com/news/earnings/262079031-tradingkey (source_type: other)
[4] Zillow says its 'Housing Super App' strategy is working - https://www.housingwire.com/articles/zillow-q2-2026-earnings (source_type: other)
[5] Zillow Group Reports First-Quarter 2026 Financial Results - https://www.prnewswire.com/news-releases/zillow-group-reports-first-quarter-2026-financial-results-302764351.html (source_type: major_news)
[6] Zillow Group Reports Second-Quarter 2026 Financial Results - https://investors.zillowgroup.com/news-and-events/news/news-details/2026/Zillow-Group-Reports-Second-Quarter-2026-Financial-Results/default.aspx (source_type: company_site, name match confirmed)
[7] John Holland LinkedIn post - https://www.linkedin.com/in/johnholland85 (source_type: unverified: social/video)
[8] Okta Customer Award Winners blog - https://www.okta.com/blog/customers-and-partners/honoring-identity-innovation--meet-the-2025-okta-customer-award- (source_type: unverified: blog)