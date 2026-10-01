# Pre-call brief: Zillow

## 1. Deal snapshot
- **Stage:** Expansion - Discovery [1]
- **ARR:** $140,000 [1]
- **Close/renewal date:** 2026-12-01 [1]
- **Owner:** Alex Kim [1]
- **Champion:** Director of DevOps [1]
- **Last activity:** 2026-09-11 — workshop on secrets management for DevOps [1]
- **Rep notes:** Existing Enterprise customer; evaluating us vs. HashiCorp Vault for secrets management. DevOps team prefers our UX, but the security architecture team prefers Vault [1].

## 2. Company context
- **HQ:** Seattle, WA [2]
- **Size:** 6,000 employees per CRM [1]; enrichment shows 5,000–10,000 employee band, $1B–5B revenue band [2]
- **Ownership:** Public [2]
- **Identity provider:** Okta [2]
- **Relevant tech stack:** AWS, Kubernetes, Terraform, and HashiCorp Vault (currently in pilot) [2]

## 3. Recent signals
No relevant recent news found. Web searches for Zillow secrets management/Vault activity, general security news, and CISO/DevOps leadership changes returned only unrelated, low-quality, or off-topic results (unrelated companies, generic blogs, or non-security leadership items such as a new legal chief mention) [3]. None met the bar for a reliable, on-topic signal.

## 4. Risks and open questions
- Competitive risk: Vault is already piloted internally and has a champion in the security architecture team, while our champion is in DevOps — internal split could stall or kill expansion [1][2].
- Open question: Who owns the final buying decision — DevOps or security architecture — and what would it take to win over the latter?
- Data gap: No named individual for the "Director of DevOps" champion or security architecture counterpart on file [1].
- Data gap: No recent public news corroborates or contradicts the internal Vault-vs-us narrative; can't confirm if Vault pilot has expanded or stalled externally.
- Inference: Given Okta as IdP and AWS/Kubernetes/Terraform stack, integration story should emphasize compatibility with existing Okta SSO and Terraform workflows [2].

## 5. Talking points
1. Reinforce UX advantage already recognized by DevOps from the 9/11 workshop — ask what specifically resonated and what objections remain [1].
2. Directly address the Vault pilot: ask what criteria the security architecture team is using to evaluate Vault vs. us, and offer a head-to-head technical session [1][2].
3. Highlight integration with their existing Okta SSO and Terraform-based infrastructure as a differentiator/reducer of migration friction [2].
4. Inference: Since Zillow is already an Enterprise customer, frame this as a low-risk expansion (add-on to existing trusted relationship) rather than a rip-and-replace of Vault.
5. Ask directly about decision timeline relative to the 2026-12-01 renewal date to ensure expansion and renewal conversations are aligned [1].

## Sources
[1] crm_accounts.csv, ACC-007
[2] firmographics.csv (mock_enrichment_v1)
[3] Web search results for "Zillow HashiCorp Vault OR secrets management 2026", "Zillow security news 2026", and "Zillow CISO OR DevOps leadership 2026" — no on-topic, reliable results found (queried 2026-09-30)