# Data Dictionary

All data in this folder is **synthetic**. Company names are real in 16 of 18 accounts so the agent's web-search tool can find genuine public news, but every CRM and firmographic value (deal stage, ARR, contacts, notes, tech stack, etc.) is invented for demonstration. Two accounts (Harborline Freight Co., Mesa Verde Dental Group) are fully fictional.

The data represents the CRM of a fictional password-security / secrets-management vendor.

## crm_accounts.csv — internal CRM records (one row per account)

| Field | Type | Definition |
|---|---|---|
| account_id | text | Unique internal ID (ACC-###). |
| account_name | text | Company name as recorded in the CRM. May include an alias in parentheses, e.g. "Instacart (Maplebear)". |
| industry | text | Industry classification entered by the sales team. |
| employee_count | integer | Approximate headcount as recorded by the rep (may differ from the enrichment band). |
| deal_stage | text | Current motion and stage: `Renewal - N days out`, `Expansion - <stage>`, `New business - <stage>`, or `Closed lost - revisit`. |
| product_interest | text | Product tier or add-on in play: Business, Enterprise, SSO/SCIM add-on, Secrets Automation. |
| arr_usd | integer | Current annual recurring revenue from the account, in USD. Blank for prospects that are not yet customers. |
| close_or_renewal_date | date (YYYY-MM-DD) | Expected close date (new business / expansion) or contract renewal date (renewals). |
| account_owner | text | Sales rep who owns the account. Blank = unassigned. |
| champion | text | Title of the main internal advocate at the customer. Blank = no champion identified. |
| last_activity | text | Date and short description of the most recent logged sales activity. |
| open_notes | text | Free-text rep notes: risks, context, next steps. Unstructured and may be incomplete or contradictory. |

## firmographics.csv — mock enrichment data (stands in for a ZoomInfo-style provider)

| Field | Type | Definition |
|---|---|---|
| account_name | text | Company name, used to join to the CRM. |
| hq_location | text | Headquarters city and state. |
| employee_band | text | Headcount range from the enrichment provider. |
| revenue_band | text | Annual revenue range. |
| ownership | text | Public, Private, Private (PE-owned), or Nonprofit. |
| identity_provider | text | Primary identity/SSO platform (e.g. Okta, Microsoft Entra ID). Blank = unknown. |
| tech_stack_notes | text | Other notable technologies detected. Blank = unknown. |
| data_source | text | Provenance label for the record (`mock_enrichment_v1`), so the agent can cite where a fact came from. |

## Deliberate data-quality test cases

These gaps are intentional and are used in the evaluation to check that the agent flags missing or conflicting data instead of inventing it.

| Account | Condition |
|---|---|
| Rivian | Most CRM fields blank (no champion, activity, or notes). |
| Mesa Verde Dental Group | No firmographic record. |
| Harborline Freight Co. | Fictional company: web search should return nothing relevant. |
| JetBlue | Contradictory notes about whether the champion left the company. |
| Patagonia | No account owner; sparse enrichment data. |
| Carvana | Closed-lost account; no identity provider in enrichment. |
| Instacart (Maplebear) | Name alias: lookup must match "Instacart" or "Maplebear". |
