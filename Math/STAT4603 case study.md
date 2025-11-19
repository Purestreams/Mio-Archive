# Case Study

Here is an analysis of the case studies based on the risk categories you provided.

---

## 1. Long-Term Capital Management (LTCM)

### Summary
Long-Term Capital Management (LTCM) was a highly leveraged hedge fund founded by famed traders and Nobel-prize-winning economists. The fund's primary strategy involved quantitative "convergence trades," betting that mispriced securities would revert to their historical relationships. The models assumed high correlation and low risk. In 1998, the Russian sovereign default triggered a global "flight to liquidity" that caused the fund's positions to diverge dramatically rather than converge. Facing catastrophic losses and margin calls, the fund collapsed and required a \$3.5 billion bailout orchestrated by the Federal Reserve to prevent a systemic financial crisis.

### Key Risk Factors Analysis

* **Valuation and Risk Models, Market Risk:** This was a primary failure. LTCM's sophisticated models depended on historical correlations that broke down under market stress. The fund's managers mistook model-based "fair value" for "market value," believing their "patient capital" could outlast any short-term volatility. Their models failed to account for liquidity as a distinct risk factor, leading to a massive, unhedged bet against market liquidity.
* **Liquidity Risk:** This was the "ultimate cause" of the fund's demise. LTCM's strategy was essentially short highly liquid assets (like on-the-run Treasuries) and long illiquid assets (like off-the-run Treasuries). When the "flight to quality" began, lenders lost patience and made margin calls. LTCM could not sell its illiquid assets to meet these calls without incurring massive losses, triggering a "downward spiral".
* **Credit Risk:** This was the "proximate cause" or trigger. The crisis began when Russia defaulted on its government debt. LTCM's hedge for this position also failed when the banks guaranteeing their ruble trades shut down, leaving them exposed.
* **Firm-wide Risk Management:** The firm's entire strategy was built on a high-leverage (roughly 30:1) foundation. This leverage magnified the model failures and liquidity crunch. The firm's partners had a massive, concentrated, and unhedged exposure to a single risk factor—a global liquidity crisis—that their models said was impossible. The crisis also revealed that many other financial institutions had failed to aggregate their own risk exposures, as they had all copied LTCM's trades.

---

## 2. Barings Bank

### Summary
The 1995 collapse of Barings Bank, one of the UK's oldest banks, was caused by the fraudulent activities of a single "rogue trader," Nick Leeson, in Singapore. Leeson was officially supposed to be conducting risk-free arbitrage on Nikkei 225 futures. However, due to a catastrophic lack of internal controls, he was in charge of both the front office (trading) and the back office (settlements), allowing him to hide his activities. He used a secret error account (88888) to hide massive, unhedged long positions on the Nikkei. When the Kobe earthquake in 1995 caused the market to crash, the resulting margin calls created losses of \$1.4 billion, more than double the bank's entire capital. The bank was declared bankrupt and sold for £1.

### Key Risk Factors Analysis

* **Operational Risk:** This was the root cause of the disaster. The bank's failure to **segregate duties**—allowing Leeson to be in charge of both trading and settlement—was a critical breakdown in internal controls. This "d dreadful power" enabled him to single-handedly "check and to know if the records matched the actual sales" and hide his losses in the secret 88888 account.
* **Market Risk:** This was the risk Leeson actually took. He abandoned his risk-free arbitrage mandate and took a massive, unhedged, and highly leveraged directional bet (a long position) on the Nikkei 225 futures market. He was betting the market would rise, but the unexpected Kobe earthquake caused it to plummet, wiping out his position.
* **Firm-wide Risk Management:** Senior management had a complete lack of oversight. They had "lots of trust" in Leeson, viewing him as a "star trader" responsible for a large portion of the bank's profits. They failed to question the glaring operational risk of his dual role or the massive, unhedged positions he was building. They believed his publicly known positions were hedged, as he claimed, when in fact they were not.

---

## 3. Bear Stearns

### Summary
Bear Stearns was an 85-year-old investment bank with a high-risk, "aggressive trading" culture and very high leverage (36:1). The firm was a pioneer and a major player in the securitization of subprime mortgages. In 2007, two of its sponsored hedge funds, which were heavily invested in these "unmarketable" mortgage derivatives, collapsed. This event shattered market confidence in the firm and its valuations. In March 2008, this led to a "run on the bank" as clients and counterparties pulled their cash. The firm "burned through nearly \$18 billion in cash reserves" in a week, and the Federal Reserve had to provide emergency financing and broker a fire sale to JPMorgan Chase to prevent a systemic collapse.

### Key Risk Factors Analysis

* **Liquidity Risk:** This was the immediate cause of failure. The collapse of the firm's hedge funds in 2007 created a crisis of confidence. This triggered a "good old fashioned run on the bank". Lenders refused to renew credit lines and clients pulled billions in assets. The firm simply ran out of cash to fund its operations, despite its CEO publicly insisting the firm's liquidity was "strong".
* **Credit Risk:** This was the underlying asset risk. The firm's "outsized position in subprime mortgages" and related derivatives was a massive bet on the creditworthiness of subprime borrowers. When those borrowers began to default, the value of these "toxic assets" collapsed, triggering the 2007 hedge fund failure and the 2008 crisis of confidence.
* **Valuation and Risk Models, Market Risk:** The firm was heavily concentrated in complex, "thinly traded" mortgage derivatives (CDOs) that were "unmarketable" in a crisis. When the market seized, these assets could not be sold and were impossible to value, sparking "fears that the Bear Stearns funds may need to dump assets". The firm's 36:1 leverage ratio meant it had almost no capital to absorb the market-value losses on these assets.
* **Firm-wide Risk Management:** The firm's aggressive culture, focused on "immediate opportunistic returns with little long term strategic planning", led it to take on excessive risk and leverage. Even after the 2007 hedge fund collapse warned of the danger, management failed to "augment its capital... or reduce its large and growing inventory of weak assets". Furthermore, the SEC's voluntary "Consolidated Supervised Entities (CSE)" program, which was supposed to provide oversight, was "inadequate" and failed to take action despite being aware of the firm's risk concentration.

---

## 4. JPMorgan Chase (London Whale)

### Summary
In 2012, JPMorgan's Chief Investment Office (CIO), which was meant to hedge the bank's overall risk, accumulated a massive position in synthetic credit derivatives. These trades, managed by Bruno Iksil (the "London Whale"), breached the CIO's Value at Risk (VaR) limit. Instead of reducing the position, the CIO responded by adopting a new, flawed VaR model that had "formula and calculation errors" and immediately cut the reported VaR by half, masking the true risk. Managers repeatedly dismissed breaches of other key risk metrics (like CRM and CSBPV) as "garbage" or "outdated". Only when the "overriding" CSW10% limit was breached did the head of the CIO, Ina Drew, halt trading. The fiasco ultimately cost the bank \$6.2 billion.

### Key Risk Factors Analysis

* **Valuation and Risk Models, Market Risk:** This was a deliberate manipulation of risk models. When the CIO's market risk breached the existing VaR limit, the unit switched to a new, "inadequate" model that was "not properly implemented". This new model incorrectly lowered their reported risk, allowing them to continue trading. The firm was also unable to calculate another key metric, the Comprehensive Risk Measure (CRM), for a critical five-week period; when it was finally calculated, it showed a massive \$6.3 billion risk, which was remarkably close to the final loss.
* **Operational Risk:** This was a failure of both systems and governance. The flawed new VaR model was implemented via a "cumbersome" process of manually entering data into spreadsheets, which was "prone to error". The bank's Model Review Group approved the new model without sufficient "back-testing" or "parallel testing". Furthermore, the JPM Task Force later found that traders had not complied with accounting principles in valuing their positions, in an effort to "hide their losses".
* **Firm-wide Risk Management:** This was a complete breakdown of the risk management framework. Breaches of Level 1 and Level 2 risk limits were repeatedly ignored, dismissed, or "solved" by changing the model. When the firm-wide VaR limit was breached, senior management approved a *temporary increase* in the limit, trusting the CIO's flawed new model would fix the problem. Managers like Ina Drew and Peter Weiland actively disparaged and disregarded metrics (like CSBPV and CRM) that correctly identified the risk. The CIO also operated with no specific limits for the Synthetic Credit Portfolio itself.

---

## 5. Fannie Mae & Freddie Mac

### Summary
Fannie Mae and Freddie Mac were Government-Sponsored Enterprises (GSEs) created to provide liquidity and support to the US mortgage market. Beginning in the 1990s, they faced intense political pressure from Congress and the Clinton and Bush administrations to meet affordable housing goals. This pressure forced them to ease their credit standards and guarantee or purchase trillions of dollars in risky, subprime, and "layered-risk" loans. Their risk models, designed for "plain vanilla" loans, were incapable of accurately assessing the risk of these new products. When the housing market collapsed in 2007-2008, the GSEs faced "mounting losses" from foreclosures that wiped out their capital. To prevent the collapse of the entire financial system, the US government placed them into conservatorship in September 2008.

### Key Risk Factors Analysis

* **Credit Risk:** This was the central cause of the failure. The GSEs' business model shifted from backing safe, conforming mortgages to guaranteeing a massive portfolio of high-risk subprime and Alt-A loans to borrowers with poor credit. When the housing bubble burst, widespread borrower defaults materialized this credit risk, causing "mounting losses" that the companies' capital could not cover.
* **Valuation and Risk Models, Market Risk:** The GSEs "over-estimated the power and accuracy of their computer systems". Their models were built to analyze "plain vanilla loans" and could not "fully analyze" or "correctly" identify the dangers of the new, complex "layered-risk" products (like interest-only, teaser rate, and low-doc loans) they were pushed to buy.
* **Operational Risk:** A key operational risk was **political interference**. The firms were "pressured by the Clinton administration in 1999" and later the Bush administration to expand risky lending to meet "affordable housing goals". This political lobbying "held off major criticism" and "postponed strengthening regulatory oversight", allowing the risk to build unchecked.
* **Firm-wide Risk Management:** The firms "grew rapidly... without adequate capital to protect them from unexpected losses". Management "initially played down the dangers posed by an inflated housing market". Their special status as GSEs created a massive moral hazard, as the market perceived an "implicit government guarantee". This allowed them to "borrow at will" at low rates and avoid raising the necessary capital to weather the storm.