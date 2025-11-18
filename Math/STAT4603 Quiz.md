# STAT4603 QUIZ paper 2023 Sem 1

## Question 1

Given below the performance ratios of two funds, A & B, over last 12 months.
Assume risk-free rate at 6.0% and benchmark returns is 5.0%

| | Sharpe ratio | Information ratio | Tracking error | $\beta$ |
| :--- | :---: | :---: | :---: | :---: |
| **Fund A** | 5.0 | 3.5 | 5.6% | 1.30 |
| **Fund B** | 3.4 | 2.6 | 3.1% | 1.45 |


### a) Use the given ratios, deduce the average rate of returns and absolute risks for Fund A and Fund B, respectively. i.e. Find $\mu_A$, $\mu_B$, $\sigma_A$, and $\sigma_B$.

**Given:**
* Risk-Free Rate ($r_f$): 6.0%
* Benchmark Return ($\mu_{BM}$): 5.0%
* Formulas:
    * Information Ratio (IR) = $\frac{\mu_p - \mu_{BM}}{w}$ (where $w$ = Tracking Error)
    * Sharpe Ratio (SR) = $\frac{\mu_p - r_f}{\sigma_p}$

---

**Step 1: Calculate Average Rate of Returns ($\mu_A$ and $\mu_B$)**

We use the Information Ratio (IR) formula to find the average returns.

* **For Fund A ($\mu_A$):**
    * $IR_A = \frac{\mu_A - \mu_{BM}}{TE_A}$
    * $3.5 = \frac{\mu_A - 5.0\%}{5.6\%}$
    * $\mu_A = (3.5 \times 5.6\%) + 5.0\%$
    * $\mu_A = 19.6\% + 5.0\% = \mathbf{24.6\%}$

* **For Fund B ($\mu_B$):**
    * $IR_B = \frac{\mu_B - \mu_{BM}}{TE_B}$
    * $2.6 = \frac{\mu_B - 5.0\%}{3.1\%}$
    * $\mu_B = (2.6 \times 3.1\%) + 5.0\%$
    * $\mu_B = 8.06\% + 5.0\% = \mathbf{13.06\%}$

**Step 2: Calculate Absolute Risks ($\sigma_A$ and $\sigma_B$)**

We use the Sharpe Ratio (SR) formula and the returns calculated in Step 1 to find the absolute risk (standard deviation).

* **For Fund A ($\sigma_A$):**
    * $SR_A = \frac{\mu_A - r_f}{\sigma_A}$
    * $5.0 = \frac{24.6\% - 6.0\%}{\sigma_A}$
    * $\sigma_A = \frac{18.6\%}{5.0}$
    * $\sigma_A = \mathbf{3.72\%}$

* **For Fund B ($\sigma_B$):**
    * $SR_B = \frac{\mu_B - r_f}{\sigma_B}$
    * $3.4 = \frac{13.06\% - 6.0\%}{\sigma_B}$
    * $\sigma_B = \frac{7.06\%}{3.4}$
    * $\sigma_B = 2.076...\% \approx \mathbf{2.08\%}$

### b) Find Treynor ratio for Fund A and Fund B, respectively.

**Given:**
* Formula: Treynor Ratio (TR) = $\frac{\mu_p - r_f}{\beta_p}$
* Values from part (a): $\mu_A = 24.6\%$, $\mu_B = 13.06\%$
* Given values: $\beta_A = 1.30$, $\beta_B = 1.45$, $r_f = 6.0\%$

---

* **For Fund A ($TR_A$):**
    * $TR_A = \frac{24.6\% - 6.0\%}{1.30}$
    * $TR_A = \frac{18.6\%}{1.30}$
    * $TR_A = 14.307...\% \approx \mathbf{14.31\%}$

* **For Fund B ($TR_B$):**
    * $TR_B = \frac{13.06\% - 6.0\%}{1.45}$
    * $TR_B = \frac{7.06\%}{1.45}$
    * $TR_B = 4.868...\% \approx \mathbf{4.87\%}$

### c) Give your analysis for the performance of Fund A and Fund B. Which Fund would you choose? Give your reasons.

**Analysis:**

To compare the two funds, we should look at their risk-adjusted performance ratios.

1.  **Sharpe Ratio (SR):**
    * $SR_A = 5.0$
    * $SR_B = 3.4$
    * The Sharpe ratio measures the excess return (above the risk-free rate) per unit of **total risk** (standard deviation).
    * **Fund A provides a much higher return for each unit of total risk taken.**

2.  **Information Ratio (IR):**
    * $IR_A = 3.5$
    * $IR_B = 2.6$
    * The Information ratio measures the active return (above the benchmark) per unit of **active risk** (tracking error). This is a key measure of an active manager's skill.
    * **Fund A demonstrates superior skill in generating returns that deviate from the benchmark.**

3.  **Treynor Ratio (TR):**
    * $TR_A = 14.31\%$
    * $TR_B = 4.87\%$
    * The Treynor ratio measures the excess return per unit of **systematic risk** (beta).
    * **Fund A generates significantly more return for each unit of market risk it takes on.**

**Conclusion:**

**I would choose Fund A.**

Fund A outperforms Fund B on all three key risk-adjusted performance metrics. It is more efficient at generating returns relative to its total risk (Sharpe), its active risk (Information), and its systematic risk (Treynor). Despite Fund A having a higher absolute risk ($\sigma_A = 3.72\%$) than Fund B ($\sigma_B = 2.08\%$), its much higher average return ($\mu_A = 24.6\%$ vs. $\mu_B = 13.06\%$) more than compensates for this, as demonstrated by its superior ratios.

---

## Question 2

The graph shows the TED spreads between July 2006 and July 2009.

### a) Define "TED Spread"? What does TED spread indicate?

**Definition:**
The **TED spread** is the difference (or "spread") between the interest rate on 3-month **E**urodollar contracts (often proxied by LIBOR) and the interest rate on 3-month U.S. **T**reasury bills (T-bills).

* **Eurodollar Rate (proxied by \$LIBOR):** This represents the rate at which major international banks lend to one another. It includes a premium for perceived **credit risk** (counterparty risk).
* **T-bill Rate (proxied by USGG3M):** This is the interest rate paid by the U.S. government. It is considered the **risk-free rate** because the government is deemed to have zero default risk.

**Indication:**
The TED spread is a key indicator of **perceived credit risk and stress in the global banking system**.

* **A high or widening spread** indicates that banks perceive a high risk in lending to each other (high counterparty risk). They demand a much higher interest rate (LIBOR) compared to the risk-free rate. This signals a **"flight to quality"** and a lack of trust (i.e., a liquidity squeeze or credit crisis).
* **A low or narrow spread** indicates that banks feel confident lending to one another at rates very close to the risk-free rate. This signals a healthy, low-risk banking environment.

### b) Describe what happened with the TED spread after the Lehman's bankruptcy on September 15, 2008.

Based on the graph:

1.  Lehman Brothers filed for bankruptcy on September 15, 2008, which falls on the timeline between "1 July 2008" and "1 January 2009".
2.  Immediately following this event, the **TED spread (the thick red line) spiked dramatically**.
3.  It exploded from a pre-crisis level of around 1-2% to its **all-time peak of nearly 5%** (around 4.8%) in October 2008.
4.  This spike was caused by the **LIBOR rate (thin green line) shooting up** as banks panicked and refused to lend to each other, while the **T-bill rate (dashed blue line) plummeted to near-zero** as investors desperately sought the safety of U.S. government debt.
5.  This extreme widening represented a complete seizure of the interbank lending market and was the acute phase of the Global Financial Crisis.

### c) What are the impacts for the low-rating financial institutions during the period?

During the period of an extremely high TED spread (like late 2008), low-rating financial institutions would face catastrophic impacts:

* **Funding Liquidity Crisis:** The high TED spread meant the interbank lending market, which these institutions rely on for short-term funding, had frozen. No one was willing to lend, especially to an institution already perceived as "low-rating" (risky).
* **Inability to Roll Over Debt:** They would be unable to get new short-term loans to pay off existing short-term debts that were coming due.
* **Exorbitant Funding Costs:** If they could find funding at all, the interest rate would be prohibitively high (the already-high LIBOR rate plus an even larger credit spread due to their low rating). This would quickly destroy their profitability.
* **Insolvency:** This acute funding liquidity crisis would rapidly lead to a solvency crisis. Without cash to meet their immediate obligations, they would be forced to default and file for bankruptcy, just as Lehman Brothers did.

---

## Question 3

The following table shows the trading records of a trader investing in an equity share at different times of a particular trading day.

| Time | Bid Price | Ask Price | Shares bought |
| :--- | :---: | :---: | :---: |
| 10:30 (T1) | 23.8 | 24.8 | 10,000 |
| 11:20 (T2) | 24.6 | 25.2 | 12,000 |
| 12:28 (T3) | 25.4 | 26.2 | 8,000 |


### a) What are the mid-price values $(\alpha_{i})$ of the positions at T1, T2 and T3, respectively?

The mid-price is the average of the bid and ask prices: $\alpha = \frac{\text{Bid} + \text{Ask}}{2}$.

* **T1:** $\alpha_1 = \frac{23.8 + 24.8}{2} = \mathbf{24.3}$
* **T2:** $\alpha_2 = \frac{24.6 + 25.2}{2} = \mathbf{24.9}$
* **T3:** $\alpha_3 = \frac{25.4 + 26.2}{2} = \mathbf{25.8}$

### b) What are the proportional bid-ask spreads $(s_{i})$ for T1, T2 and T3, respectively?

The proportional (or relative) bid-ask spread is the dollar spread divided by the mid-price: $s = \frac{\text{Ask} - \text{Bid}}{\alpha}$ (where $\alpha$ is $P_{mid}$).

* **T1:** $s_1 = \frac{24.8 - 23.8}{24.3} = \frac{1.0}{24.3} = 0.04115... \approx \mathbf{0.0412}$
* **T2:** $s_2 = \frac{25.2 - 24.6}{24.9} = \frac{0.6}{24.9} = 0.02409... \approx \mathbf{0.0241}$
* **T3:** $s_3 = \frac{26.2 - 25.4}{25.8} = \frac{0.8}{25.8} = 0.03100... \approx \mathbf{0.0310}$

### c) Find the cost of liquidation under the normal market condition.

The cost of liquidation for a long position (shares were bought) is the cost of selling all shares at the bid price. This cost is the difference between the mid-price and the bid price (which is half the dollar spread) multiplied by the number of shares.

Cost = $\sum (\text{Shares}_i \times \frac{\text{Ask}_i - \text{Bid}_i}{2})$

* **T1 Cost:** $10,000 \times (\frac{24.8 - 23.8}{2}) = 10,000 \times 0.5 = 5,000$
* **T2 Cost:** $12,000 \times (\frac{25.2 - 24.6}{2}) = 12,000 \times 0.3 = 3,600$
* **T3 Cost:** $8,000 \times (\frac{26.2 - 25.4}{2}) = 8,000 \times 0.4 = 3,200$

**Total Normal Cost** = $5,000 + 3,600 + 3,200 = \mathbf{\$11,800}$

### d) ...Calculate the means and standard deviations of the proportional bid-ask spreads for the three respective trades.

**Given:**
* Mean of *dollar* spread ($\mu_S$): 0.8
* Standard deviation of *dollar* spread ($\sigma_S$): 0.2
* Formulas:
    * Mean of proportional spread: $\mu_{s,i} = \frac{\mu_S}{\alpha_i}$
    * St. dev. of proportional spread: $\sigma_{s,i} = \frac{\sigma_S}{\alpha_i}$

---

* **T1:**
    * $\mu_{s,1} = \frac{0.8}{24.3} = 0.03292... \approx \mathbf{0.0329}$
    * $\sigma_{s,1} = \frac{0.2}{24.3} = 0.00823... \approx \mathbf{0.0082}$

* **T2:**
    * $\mu_{s,2} = \frac{0.8}{24.9} = 0.03212... \approx \mathbf{0.0321}$
    * $\sigma_{s,2} = \frac{0.2}{24.9} = 0.00803... \approx \mathbf{0.0080}$

* **T3:**
    * $\mu_{s,3} = \frac{0.8}{25.8} = 0.03100... \approx \mathbf{0.0310}$
    * $\sigma_{s,3} = \frac{0.2}{25.8} = 0.00775... \approx \mathbf{0.0078}$

### e) At 99% confidence level $(\lambda=2.326)$, what is the cost of liquidation under the stressed market assumption?

The stressed cost of liquidation is calculated using a 99% confidence level "stressed spread" ($s^*$).
The formula for stressed liquidity cost is $L_2 = W \times \frac{1}{2}(\overline{S} + \alpha~\sigma_{S})$ from the formula sheet, where $W$ is the value of the position, $\overline{S}$ is the mean proportional spread $\mu_{s,i}$, and $\alpha$ is the confidence level $\lambda$.

Cost$_{stressed}$ = $\sum (\frac{V_i}{2} \times s^*_i) = \sum (\frac{\text{Shares}_i \times \alpha_i}{2} \times (\mu_{s,i} + \lambda \sigma_{s,i}))$

* **Position Values ($V_i = \text{Shares}_i \times \alpha_i$):**
    * $V_1 = 10,000 \times 24.3 = 243,000$
    * $V_2 = 12,000 \times 24.9 = 298,800$
    * $V_3 = 8,000 \times 25.8 = 206,400$

* **Stressed Spreads ($s^*_i = \mu_{s,i} + \lambda \sigma_{s,i}$):**
    * $s^*_1 = 0.0329 + (2.326 \times 0.0082) = 0.0329 + 0.0190732 = 0.0519732$
    * $s^*_2 = 0.0321 + (2.326 \times 0.0080) = 0.0321 + 0.018608 = 0.050708$
    * $s^*_3 = 0.0310 + (2.326 \times 0.0078) = 0.0310 + 0.0181428 = 0.0491428$

* **Stressed Costs:**
    * **T1 Cost:** $\frac{243,000}{2} \times 0.0519732 = 121,500 \times 0.0519732 = 6,314.75$
    * **T2 Cost:** $\frac{298,800}{2} \times 0.050708 = 149,400 \times 0.050708 = 7,575.88$
    * **T3 Cost:** $\frac{206,400}{2} \times 0.0491428 = 103,200 \times 0.0491428 = 5,071.54$

**Total Stressed Cost** = $6,314.75 + 7,575.88 + 5,071.54 = \mathbf{\$18,962.17}$
(This matches the value of $18,961.7$ in the test paper, with minor differences due to rounding).

### f) Comment the change in the cost of liquidation under normal and stressed market assumptions.

* **Normal Liquidation Cost:** \$11,800
* **Stressed Liquidation Cost (99% CI):** \$18,962.17

**Comment:**
The cost of liquidation under the 99% stressed market assumption is **\$18,962.17**, which is **\$7,162.17 (or 60.7%) higher** than the normal market cost of \$11,800.

This significant increase demonstrates the impact of **liquidity risk**. In a stressed market, bid-ask spreads not only widen (higher mean) but also become more volatile (higher standard deviation). The stressed calculation captures this "worst-case" scenario, showing that the cost to exit a position can increase dramatically when market conditions deteriorate, precisely when a trader might be forced to sell.

---

## Question 4

### a) Describe LTCM's trading strategies and how the firm accumulated substantial financial risks prior to the fall of the firm.

**Trading Strategies:**
Long-Term Capital Management (LTCM) was a hedge fund known for its **fixed-income arbitrage** and **convergence trading** strategies. These strategies were developed by academics and traders using complex quantitative models to identify small, temporary pricing discrepancies between similar securities.

* **Primary Strategy:** Their main bet was that the prices of "cheap" and "expensive" but economically similar assets would eventually "converge."
* **Example (Treasury Bonds):** They would long (buy) "off-the-run" (older, less liquid) U.S. Treasury bonds and simultaneously short (sell) "on-the-run" (newly issued, more liquid) Treasury bonds. The off-the-run bonds traded at a small discount due to their lower liquidity. LTCM bet this liquidity spread would narrow.
* **Other Trades:** They applied this same logic globally, including swap-spread arbitrage (betting the spread between swap rates and government bonds would narrow) and volatility trading (shorting options, betting that market volatility would remain low).

**Risk Accumulation:**
LTCM accumulated substantial risk through two primary mechanisms:

1.  **Massive Leverage:** The profit margins on their convergence trades were extremely small (often just a few basis points). To generate their target returns, LTCM borrowed enormous amounts of money to amplify their positions. Their on-balance-sheet leverage was over 25:1, but their *effective* leverage, using off-balance-sheet derivatives, was estimated to be much higher, perhaps over 100:1.
2.  **Concentration & Model Risk:** Although they traded in many different markets, most of their positions were fundamentally the same bet: that "risk" (as defined by their historical models) was low and that markets would remain orderly and converge. This was a massive, concentrated bet on low volatility. When a global shock (the 1998 Russian default) occurred, all these "uncorrelated" positions suddenly moved against them at once, as investors globally fled from *all* risky/illiquid assets (like LTCM's "cheap" bonds) and piled into the most liquid, safe assets (like LTCM's "expensive" shorts). Their models, based on historical data, failed to predict this systemic "flight to quality."

### b) Use LTCM as an example to demonstrate its asset liquidity risk that the firm has exposed to and hence lend itself to failure.

**Asset liquidity risk** is the risk that an asset cannot be sold quickly without incurring a significant price concession (i.e., at a "fire sale" price). LTCM's failure is a classic example of this risk.

1.  **Funding vs. Asset Liquidity:** When the 1998 Russian crisis caused LTCM's trades to lose money, their lenders (investment banks) made **margin calls**, demanding more collateral. This was a **funding liquidity** problem (a need for cash).
2.  **Liquidation Attempt:** To raise this cash, LTCM was forced to liquidate (sell) its assets. This is where **asset liquidity risk** materialized.
3.  **Illiquid Positions:** Many of LTCM's positions were in niche, relatively illiquid markets. Furthermore, LTCM *was* the market in many of these assets; their positions were so enormous that there were not enough natural buyers to absorb the sales without the price collapsing.
4.  **Predatory Trading:** Other market participants (including some of their own lenders) knew LTCM was in trouble and knew what their positions were. They engaged in predatory trading, either "front-running" (selling the same assets LTCM needed to sell, driving prices down further) or refusing to bid, knowing LTCM was a forced and desperate seller.
5.  **The Vicious Spiral:** This created a death spiral:
    * Margin calls forced LTCM to sell assets.
    * Selling illiquid assets into a panicked market caused their prices to crash.
    * This "fire sale" resulted in massive realized losses.
    * These new, larger losses triggered even more margin calls.

Ultimately, LTCM failed because its assets were illiquid. They could not be sold at their "model" value (or anywhere close to it) to meet their funding needs. This forced the U.S. Federal Reserve to orchestrate a bailout, precisely because the systemic risk of LTCM's fire-sale liquidations collapsing the entire financial system was too high.