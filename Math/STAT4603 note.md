# STAT4603 Note

## Chapter 1: Foundations of Risk Management

### 1.1 What is Risk Management?
Financial risk management is the process of identifying, assessing, measuring, and managing financial risks. It utilizes quantitative tools and judgment and is often centralized within an institution to provide a top-level view of risk.

### 1.2 Risk Measurement
Risk is measured by analyzing the probability distribution of future profits and losses (P&L) for a portfolio.



Key metrics from this distribution include:
* **Mean ($\mu$):** The average return, or the center of the distribution.
* **Standard Deviation ($\sigma$):** Also known as **volatility**, this measures the dispersion of returns around the mean.
* **Value at Risk (VAR):** The maximum loss over a target horizon such that there is a low, pre-specified probability that the actual loss will be larger. It is the cutoff percentile of the P&L distribution (e.g., a 99% confidence level VAR of 14.4% means there is a 1% chance of losing more than 14.4%).

---

### 1.3 Absolute vs. Relative Risk
* **Absolute Risk:** This measures the shortfall relative to the initial investment value, or versus cash. It is often measured by the standard deviation of the portfolio's return ($R_P$).
    * **Formula:** $\sigma(\Delta P) = \sigma(R_P) \times P$

* **Relative Risk:** This measures a portfolio's risk relative to a benchmark index (B).
    * **Tracking Error (e):** The deviation of the portfolio's return from the benchmark's return ($e = R_P - R_B$).
    * **Tracking Error Volatility (TEV or $\omega$):** The volatility of the tracking error.
    * **TEV Formula:** $\omega^2 = \sigma_P^2 - 2\rho\sigma_P\sigma_B + \sigma_B^2$

---

### 1.4 Risk-Adjusted Performance
Performance measures evaluate returns relative to the risk taken:

* **Sharpe Ratio (SR):** Measures excess return (above the risk-free rate $R_F$) per unit of **absolute risk** (total volatility). A higher SR is better.
    * **Formula:** $SR = \frac{[\mu(R_P) - R_F]}{\sigma(R_P)}$

* **Information Ratio (IR):** Measures excess return (above a benchmark $R_B$) per unit of **relative risk** (tracking error volatility). It is commonly used to compare active managers.
    * **Formula:** $IR = \frac{[\mu(R_P) - \mu(R_B)]}{\sigma(R_P - R_B)}$

* **Treynor Ratio (TR):** Measures excess return per unit of **systematic risk** ($\beta_P$).
    * **Formula:** $TR = \frac{[\mu(R_P) - R_F]}{\beta_P}$

* **Jensen's Alpha ($\alpha_P$):** Measures the actual portfolio return against the return required by the CAPM model. A positive alpha indicates outperformance.
    * **Formula:** $\alpha_P = \mu(R_P) - R_F - \beta_P[\mu(R_M) - R_F]$

---

### 1.5 Portfolio Construction & Diversification
* **Mixing Assets:** When combining assets (e.g., stocks and bonds), the portfolio's expected return is the weighted average of the individual returns. The portfolio's volatility, however, is a nonlinear function that depends on the weights, individual volatilities, and the **correlation** between the assets.
    * **Portfolio Mean:** $\mu_P = w_1\mu_1 + w_2\mu_2$
    * **Portfolio Variance:** $\sigma_P^2 = w_1^2\sigma_1^2 + 2w_1w_2(\rho\sigma_1\sigma_2) + w_2^2\sigma_2^2$

* **Diversification:** The power of diversification comes from low correlation. By combining assets with low correlation (e.g., $\rho = 0.13$), an investor can achieve the same volatility as a less risky asset (like bonds) but with a higher expected return.

* **Efficient Portfolios:** Harry Markowitz showed that for a given level of expected return, an investor should choose the portfolio with the minimum possible variance. The set of all such optimal portfolios forms the **efficient set** or "efficient frontier".

---

### 1.6 Asset Pricing Theory
* **Capital Asset Pricing Model (CAPM):** This model states that the expected return of any asset ($E(R_i)$) is equal to the risk-free rate ($R_F$) plus a risk premium. This premium is the asset's **beta ($\beta_i$)** (its systematic, non-diversifiable risk) multiplied by the market risk premium ($E(R_M) - R_F$).
    * **Formula:** $E(R_i) = R_F + \beta_i[E(R_M) - R_F]$
    * The **Capital Market Line (CML)** represents the highest possible Sharpe ratio and shows that any efficient portfolio can be formed by mixing the risk-free asset and the market portfolio.


* **Arbitrage Pricing Theory (APT):** This theory is a more general, multi-factor model. It assumes that an asset's return is driven by several independent systematic factors ($y_k$), and its expected return is based on its exposure (beta) to each of those factors.
    * **Formula:** $E[R_i] = R_F + \sum_{k=1}^{K}\beta_{ik}\lambda_k$ (where $\lambda_k$ is the risk premium for factor $k$)

---

### 1.7 Types of Risk ("Knowns and Unknowns")
* **Known Knowns:** Risks that are captured by standard risk models, like VAR. Losses should occur with the predicted low frequency.
* **Known Unknowns:** Risks that are known to exist but are not properly measured by the models. Examples include:
    * **Model Risk:** Inaccurate models, weak assumptions, or incorrect parameters. For example, UBS in 2007 used models based on a recent period of rising housing prices, which failed catastrophically.
    * **Liquidity Risk:** The risk that a position cannot be liquidated in time without a significant price impact.
* **Unknown Unknowns:** Risks that are completely outside the scope of most scenarios. Examples include sudden regulatory changes or catastrophic counterparty failures like Lehman Brothers. This is also known as **Knightian uncertainty**.

## Chapter 2: Risk Models (Market Risk)

### 2.1 Four Main Financial Risks
1.  **Market Risk:** Risk of losses from movements in financial market prices or volatilities.
2.  **Liquidity Risk:** Risk of losses from needing to liquidate positions to meet funding requirements.
3.  **Credit Risk:** Risk of losses from counterparties failing to fulfill their contractual obligations.
4.  **Operational Risk:** Risk of loss from failed internal processes, people, systems, or external events.

---

### 2.2 Value at Risk (VAR)
VAR is a key tool for market risk. It aggregates all risks across a portfolio into a single number, providing a risk measure with an associated probability.

* **Definition:** VAR is the **maximum loss** over a target horizon (e.g., 1 day) such that there is a low, pre-specified probability (e.g., 5%) that the actual loss will be larger.
* **Interpretation:** A 95% confidence VAR of $42 million means that, on average, we would expect a loss greater than $42 million on only 5% of trading days (or 5 days out of 100).



---

### 2.3 VAR Calculation Methods
There are three main methods to construct the portfolio's return distribution and calculate VAR:

1.  **Historical Simulation (HS):**
    * **How it works:** This method is non-parametric. It collects historical data of daily returns (e.g., for the last 10 years) and applies them to the *current* portfolio.
    * It then constructs a frequency distribution (histogram) of these simulated P&L outcomes and finds the quantile (e.g., the 5th percentile) that corresponds to the VAR.

2.  **Parametric (Variance-Covariance):**
    * **How it works:** This method assumes the returns follow a specific density function, typically the **normal distribution**.
    * It uses all observations to calculate the portfolio's mean ($E(X)$) and standard deviation ($SD(X)$ or $\sigma$).
    * VAR is then calculated as a multiple ($\alpha$) of this standard deviation, where $\alpha$ depends on the confidence level (e.g., $\alpha = 1.645$ for 95% confidence).
    * **Formula:** $VAR = \alpha\sigma\mathcal{W}$ (where $\mathcal{W}$ is the portfolio value).
    * **Advantage:** More precise than HS because it uses all data points.
    * **Disadvantage:** Relies on the assumption of normality, which may not hold (e.g., "fat tails").

3.  **Monte Carlo Simulation:**
    * **How it works:** This method involves assuming a particular density for the distribution of risk factors and then using a computer to draw thousands of random samples from these distributions to generate a P&L distribution for the portfolio.

---

### 2.4 VAR Caveats & Alternative Measures
* **VAR is NOT the worst-case loss:** VAR does not describe the worst possible loss; it is a loss that is expected to be exceeded with a *p* frequency.
* **VAR ignores the left tail:** VAR says nothing about the *size* of the losses once they exceed the VAR threshold. The average loss in the tail could be significantly worse than the VAR itself.

Because of these limitations, other measures are used:

* **Conditional VAR (CVAR) / Expected Shortfall (ES):**
    * **Definition:** Measures the **expected value of the loss** *given that the loss already exceeds VAR*.
    * It answers the question: "If things go bad (beyond VAR), how bad do we expect them to be on average?".
    * **Formula:** $E[X|X<q] = \int_{-\infty}^{q}xf(x)dx / \int_{-\infty}^{q}f(x)dx$

* **Semi-standard Deviation:** A measure of volatility that only considers data points representing a loss. It accounts for asymmetries (like negative skewness) in the distribution.

* **Drawdown:** The decline from a peak value to a trough value over a fixed time interval.

---

### 2.5 VAR Parameters and Basel Rules
* **Confidence Level (c):** The choice depends on the use. For daily risk management and backtesting, 95%–99% is common. For capital adequacy, a very high level is used to avoid bankruptcy.
* **Horizon (T):** The time period for the VAR. For liquid assets, a 1-day horizon is common. For capital adequacy or less liquid assets, a longer horizon (e.g., 10 days) is used.
* **Scaling VAR:** If returns are normally distributed and independent, 1-day VAR can be scaled by the square root of time.
    * **Formula:** $VAR(T~days) = VAR(1~day) \times \sqrt{T}$
* **Basel Rules (Market Risk Charge):** The Basel Accord sets minimum capital requirements for market risk, specifying:
    * A **10-day** horizon.
    * A **99%** confidence interval.
    * An observation period of at least **1 year**.

---

### 2.6 Stress Testing
* **Purpose:** VAR should always be complemented by stress-testing.
* **Definition:** Stress testing identifies situations (scenarios) that could create extraordinary but plausible losses, which may be missed by VAR models that rely on recent historical data.
* **Example:** A VAR model might miss the risk of a sudden, sharp market crash (like the 1998 exchange rate move) if such an event hasn't happened in its observation window.
* **Methods:** Includes scenario analysis (moving key variables, using historical scenarios, or creating prospective scenarios) and reverse stress tests.

## Chapter 3: Operational Risk

### 3.1 What is Operational Risk?
* **Definition (Basel Committee):** "The risk of loss resulting from **inadequate or failed internal processes, people and systems**, or from **external events**."
* This includes everything from internal fraud (rogue traders) and programming errors to external disasters or legal risk.
* It is a major cause of financial losses, sometimes even bankruptcy (e.g., Barings).

---

### 3.2 Basel Classifications
The Basel Committee classifies operational risk events into seven categories:
1.  **Internal Fraud (IF):** e.g., unauthorized activity.
2.  **External Fraud (EF):** e.g., theft, system security breaches.
3.  **Employment Practices and Workplace Safety (EPWS):** e.g., discrimination, safety violations.
4.  **Clients, Products, and Business Practices (CPBP):** e.g., product flaws, improper business practices.
5.  **Damage to Physical Assets (DPA):** e.g., natural disasters, terrorism.
6.  **Business Disruption and System Failures (BDSF):**
7.  **Execution, Delivery, and Process Management (EDPM):** e.g., transaction processing errors.

---

### 3.3 Assessing Operational Risk
* **Top-down models:** Use firm-wide or industry-wide data to determine a total capital buffer.
* **Bottom-up models:** Start at the process level to understand the *causes* of losses and then aggregate up.
* **Tools for Assessment:**
    * **Audit oversight** and **Critical self-assessment**.
    * **Key Risk Indicators (KRIs):** Simple, objective measures that act as early warning signs (e.g., employee turnover, trade volume).
    * **Actuarial Models:** Combine frequency and severity distributions.

---

### 3.4 The Loss Distribution Approach (LDA)
This is an actuarial model widely used to quantify operational risk. It combines two separate distributions:

1.  **Loss Frequency Distribution:** Models the *number* of loss events over a period (e.g., using a Poisson distribution).
2.  **Loss Severity Distribution:** Models the *size* ($) of a loss once it occurs (e.g., using a Lognormal distribution). This distribution typically has very long/fat tails, representing the small possibility of a very large loss.

These two are combined (through **Convolution**) to create an **aggregate loss distribution** for the year.



From this final distribution, risk is categorized:
* **Expected Loss (EL):** High-frequency, low-severity losses. This is treated as a cost of doing business and managed via internal controls.
* **Unexpected Loss (UL):** Lower-frequency, higher-severity events. This is the risk that must be offset by holding **economic capital**.
* **Stress Loss:** Very infrequent, extremely damaging losses in the far tail of the distribution. This risk is hard to capitalize and is often transferred via insurance.

---

### 3.5 Managing and Mitigating Operational Risk
* **Internal Controls:**
    * **Separation of Functions:** The person who commits (front office) a transaction should not be the one who clears (back office) it.
    * **Dual Entries & Reconciliations:** Matching trade tickets to confirmations and matching trader P&L estimates to middle-office calculations.
* **External Controls:**
    * **Confirmation:** Confirming trade details with the counterparty.
    * **Verification of Prices:** Using external sources to value positions.
* **Model Risk:** A key operational risk is the risk of using inappropriate pricing or risk models. This can be due to:
    * Wrong input data.
    * Incorrect parameter estimation.
    * A poor choice of model.
    * Implementation or programming errors.


---

### 3.6 Basel Operational Risk Charge (ORC)
Basel requires banks to hold capital for operational risk. It provides three methods:

1.  **Basic Indicator Approach (BIA):** The simplest method. The capital charge is a fixed percentage ($\alpha = 15\%$) of the bank's average annual gross income (GI).
    * **Formula:** $ORC^{BIA} = \alpha \times GI$
2.  **Standardized Approach (TSA):** Divides the bank into 8 business lines (e.g., retail banking, trading). A different beta factor ($\beta_i$) is applied to the gross income of each line, and the results are summed.
    * **Formula:** $ORC^{TSA} = \sum_{i=1}^{8}\beta_i \times GI_i$
3.  **Advanced Measurement Approach (AMA):** The most sophisticated. It allows banks to use their own internal models (like the LDA) to calculate the capital charge.
    * **Requirement:** The capital must cover the **Unexpected Loss (UL)** at a **99.9% confidence level** over a **one-year horizon**.
    * This requires robust internal data, use of external data, and scenario analysis.

## Chapter 4: Liquidity Risk

### 4.1 Sources of Liquidity Risk
Liquidity risk has two distinct components:

1.  **Asset Liquidity Risk (Market/Product Risk):** The risk that a position cannot be unwound or offset quickly without **significantly moving the market price**. This happens when the market lacks depth or is disrupted.
2.  **Funding Liquidity Risk:** The risk that an institution cannot meet its own liabilities and payment obligations as they come due, forcing it to incur unacceptable losses (e.g., selling assets at fire-sale prices). This risk arises from the **liability side** of the balance sheet.

---

### 4.2 Asset Liquidity Risk
This risk is a function of the **bid-ask spread**, the **time horizon** for liquidation, and the **size of the position**.



* **Bid-Ask Spread:** The difference between the offer price (where you can buy) and the bid price (where you can sell). The **mid-market price** is the average of the two.
    * **Proportional Spread:** $s = \frac{\text{offer price} - \text{bid price}}{\text{mid-market price}}$
* **Market Characteristics:**
    * **Tightness:** A measure of how close transaction prices are to the mid-market price.
    * **Depth:** The volume of trades possible without significantly affecting the price. A market with low depth is "thin".
    * **Resiliency:** The speed at which prices recover from temporary fluctuations caused by large trades.

* **Cost of Liquidation (Normal Market):** The cost to liquidate a portfolio is half the spread multiplied by the value of the position ($\alpha_i$), summed across all assets.
    * **Formula:** $\text{Cost} = \sum_{i=1}^{n}\frac{s_i \alpha_i}{2}$
    * This implies that holding many small positions is less risky than a few large ones.

* **Cost of Liquidation (Stressed Market):** This formula provides a "worst-case" liquidation cost at a given confidence level ($\lambda$). It uses the mean ($\mu_i$) and standard deviation ($\sigma_i$) of the proportional spread.
    * **Formula:** $\text{Cost (Stressed)} = \sum_{i=1}^{n}\frac{(\mu_i + \lambda\sigma_i)\alpha_i}{2}$

---

### 4.3 Liquidity-Adjusted VAR (LVAR)
Standard VAR models often assume positions can be liquidated at the mid-market price, which is unrealistic. LVAR adjusts for liquidation costs.

* **LVAR (Normal Market):** Regular VAR plus the expected cost of liquidation.
    * **Formula:** $\text{LVAR} = \text{VAR} + \sum_{i=1}^{n}\frac{s_i \alpha_i}{2}$
* **LVAR (Stressed Market):** Regular VAR plus the stressed cost of liquidation.
    * **Formula:** $\text{LVAR} = \text{VAR} + \sum_{i=1}^{n}\frac{(\mu_i + \lambda\sigma_i)\alpha_i}{2}$

---

### 4.4 Funding Liquidity Risk
This is the risk of being unable to meet payment obligations, arising from both on- and off-balance-sheet liabilities.
* **Sources of Funding:**
    * **Liabilities:** Retail deposits (stable), capital market instruments (volatile), secured funding, and unsecured funding.
    * **Off-Balance-Sheet:** Contingent claims like loan commitments, collateral calls on derivatives, or needs from Special-Purpose Vehicles (SPVs).
* **Meeting Funding Gaps:** Gaps can be met by asset sales (cash, liquid assets), using bank credit lines, or securitization.

---

### 4.5 Indicators and Management
* **Indicators:** During the 2007 crisis, liquidity risk spiked. Banks became reluctant to lend.
    * **TED Spread:** The difference between Eurodollar LIBOR (uncollateralized bank-to-bank loans) and U.S. T-bills (no credit risk). This spread, normally small, widened dramatically, reflecting high perceived credit risk and a premium for liquidity.
* **Managing Liquidity Risk:**
    * **Stress Tests:** Evaluating scenarios where cash flows deviate and funding is cut off. It's crucial to model the interaction between funding and asset liquidity risk (i.e., being forced to sell illiquid assets in a crisis).
    * **Diversification:** Using stable and diversified sources of funding (across type, geography, and maturity).
    * **Contingency Funding Plans (CFPs):** A pre-established plan of action for *how* to get funding in a crisis. This defines trigger events and lines of responsibility.

## Chapter 5: Credit Risk

### 5.1 What is Credit Risk?
* **Definition:** The risk of economic loss from a counterparty's failure to fulfill its contractual obligations. Its effect is the cost of replacing the cash flows if the other party defaults.
* For most banks, credit risk is far more significant than market risk, and the largest bank failures in history have been due to it.

---

### 5.2 Market Risk vs. Credit Risk
Credit risk differs significantly from market risk:

| Item | Market Risk | Credit Risk |
| :--- | :--- | :--- |
| **Sources** | Market movements only | Default risk, recovery risk, market risk |
| **Distributions** | Mainly symmetrical | **Skewed to the left** (small regular gains from interest/premiums, with a small chance of a large loss) |
| **Time Horizon** | Short-term (days) | Long-term (years) |
| **Aggregation** | By business/trading unit | By counterparty, across the whole firm |

---

### 5.3 Settlement vs. Pre-Settlement Risk
* **Pre-Settlement Risk:** The risk of counterparty failure *during the life* of the transaction (e.g., default on a 5-year loan). This risk exists for a long period.
* **Settlement Risk:** The risk that arises *during the settlement process* when an institution has made its payment but has not yet received the offsetting payment from the counterparty. This is a very short-term risk, often magnified by time zones (e.g., Herstatt Bank failure).
    * This risk is managed through **netting agreements** (bilateral or multilateral) and **Real-Time Gross Settlement (RTGS)** systems.

---

### 5.4 Components of Credit Loss
Credit loss is modeled using three key components:

1.  **Probability of Default (PD or $p_i$):** The likelihood that the counterparty defaults.
2.  **Credit Exposure (CE or $E[CE_i]$):** The economic value of the claim on the counterparty at the time of default. For derivatives, this is not the notional value but the replacement cost.
    * **Formula:** $CE_t = \text{Max}(V_t, 0)$ (where $V_t$ is the market value of the contract)
3.  **Loss Given Default (LGD or $E[LGD_i]$):** The fractional loss incurred *if* a default occurs. It is (1 - Recovery Rate). For example, a 30% recovery rate means a 70% LGD.

---

### 5.5 Expected vs. Unexpected Credit Loss
* **Expected Credit Loss (ECL):** The average loss expected over a period. It is the product of the three components, summed across all N instruments.
    * **Formula:** $E[CL] = \sum_{i=1}^{N} p_i \times E[CE_i] \times E[LGD_i]$
    * ECL is a cost of doing business and is typically covered by **reserves** or pricing (e.g., interest rates).

* **Unexpected Credit Loss (UCL):** The volatility or standard deviation of credit losses around the mean (ECL).
    * **Credit VaR:** A measure of the unexpected loss at a high confidence level (e.g., 95% or 99.9%). It is the difference between the worst-case loss (at the quantile) and the ECL.

    * UCL is the risk that must be covered by **economic capital**.

---

### 5.6 Credit Risk Diversification
* Diversification is crucial for managing credit risk.
* A portfolio with one $100 million loan has an EL of $1 million (at 1% PD) but a very high standard deviation of $10 million.
* A portfolio of 100 independent $1 million loans has the **same** EL of $1 million, but the standard deviation drops to just $1 million.
* **Key Principle:** As the number of independent credits (N) increases for a constant total notional, the standard deviation of the portfolio shrinks toward zero.
    * **Formula (SD for N loans):** $SD[CL] = \sqrt{p(1-p)} \times \frac{\text{\$Total Notional}}{\sqrt{N}}$

* **Correlated Defaults:** The main driver of portfolio credit risk is **correlation**. If defaults are independent, risk is low. If they are correlated (e.g., all borrowers default in a recession), diversification benefits disappear.
    * **Formula (Joint PD):** $p(A \text{ and } B) = \rho\sigma_A\sigma_B + p_A p_B$

## Chapter 6: Firm-wide Risk Management

### 6.1 Integrated Risk Management & Economic Capital
* **Integrated Risk Management:** Managing all of the firm's risks (market, credit, operational, business) in a single, consistent framework.
* **Economic Capital (EC):** The amount of capital a firm allocates to self-insure against **unexpected losses**.
    * It is a VaR-type measure set at a high confidence level over a long horizon (e.g., 1 year) to cover risks.
    * It is distinct from **reserves**, which are set aside for **expected losses**.

---

### 6.2 Risk Aggregation
A key challenge is aggregating the different types of risk.

1.  **Simple Aggregation:** Simply adding the EC for market, credit, and operational risk. This generally **overstates** the total risk because it assumes the worst-case loss occurs for all three simultaneously (i.e., perfect correlation).
2.  **Fixed Diversification:** Applying a simple reduction (e.g., 20%) to the simple sum. This is robust but not risk-sensitive.
3.  **Variance-Covariance:** Aggregating risk measures using an estimated correlation matrix. This is more sensitive but assumes linear relationships.
    * *Typical Assumptions:* High correlation between market and credit risk; very low correlation for operational risk.
4.  **Full Simulation (Copulas):** A sophisticated approach that models dependencies (including non-linear) between the different risk factor distributions.

---

### 6.3 Silo vs. Integrated Approach
* **Silo Approach:** Capital requirements are computed separately for each risk type or business unit and then added together. This ignores diversification benefits.
* **Integrated Approach:** Aggregates risk at consecutive levels (portfolio $\rightarrow$ business unit $\rightarrow$ holding company), allowing for the recognition of diversification benefits at each stage.

---

### 6.4 Risk-Adjusted Performance Measurement
Integrated risk management allows firms to evaluate the performance of business units based on the economic capital they consume.

* **Risk-Adjusted Performance Measure (RAPM):** A general term for measuring profit relative to risk capital.
    * **Formula:** $RAPM = \frac{\text{Profit}}{\text{Risk Capital (RC)}}$
    * This allows for a fair comparison: a trader with a $10M profit on $19M in capital (54% RAPM) is performing better than a trader with a $10M profit on $28M in capital (36% RAPM).

* **Risk-Adjusted Return on Capital (RAROC):** A specific type of RAPM. The "Net Profit" in the numerator is adjusted for expected losses, costs, and the return earned on the economic capital itself.
    * **Formula:** $RAROC = \frac{\text{Net Profit}}{\text{Economic Capital (EC)}}$
    * RAROC (an expected return on equity) can be compared to the firm's cost of capital to see if a project or business line adds value for shareholders.

## Chapter 7: The Basel Accord

### 7.1 Basel I (1988)
* **Purpose:** To set minimum capital requirements for commercial banks to act as a buffer against financial losses and to create a level playing field for international banks.
* **Focus:** Primarily **Credit Risk**.
* **Requirement:** Required banks to hold total capital equal to at least **8% of Risk-Weighted Assets (RWA)**. Assets were assigned risk weights (0%, 20%, 50%, 100%) based on broad categories (e.g., 0% for OECD government cash, 100% for corporate debt).

---

### 7.2 The 1996 Amendment (Market Risk)
* **Purpose:** To incorporate a capital charge for **Market Risk** as banks increased proprietary trading.
* **Key Innovation:** Separated the bank's assets into two categories:
    1.  **Trading Book:** Instruments held for short-term resale and marked-to-market (e.g., stocks, bonds, derivatives).
    2.  **Banking Book:** Instruments held to maturity, valued at historical cost (e.g., loans).
* This added a capital charge for the market risk in the trading book.

---

### 7.3 Basel II (2004)
A comprehensive revision built on three "pillars":

* **Pillar 1: Minimum Capital Requirement:**
    * Expanded the 8% rule to cover three distinct risks:
        * **Total Capital > 8% $\times$ (Credit RWA + Market RWA + Operational RWA)**
    * Provided more advanced, risk-sensitive models for calculating RWA.

* **Pillar 2: Supervisory Review Process:**
    * Requires banks to have their own internal processes for assessing capital adequacy relative to *all* risks (including those omitted from Pillar 1, like interest rate risk in the banking book).
    * Empowers supervisors to require banks to hold capital *above* the 8% minimum.

* **Pillar 3: Market Discipline:**
    * Emphasizes detailed public risk disclosures to allow market participants (investors, counterparties) to assess the bank's risk profile and capital adequacy.

---

### 7.4 Basel III (2010-2017)
* **Purpose:** A response to the 2007-2008 financial crisis, which revealed that many banks were undercapitalized despite meeting Basel II requirements.
* **Key Changes:**
    1.  **Stricter Capital Definition:** Raised the quality of capital.
        * **Core Tier 1 Capital:** Increased from 2% to 4.5%.
        * **Capital Conservation Buffer (CCB):** Added a 2.5% buffer of Core Tier 1 capital, bringing the effective minimum to **7%**.
    2.  **Leverage Ratio:** Introduced a new, non-risk-based limit on leverage to backstop the RWA calculations.
    3.  **Liquidity Requirements:** Introduced the first global minimum liquidity standards:
        * **Liquidity Coverage Ratio (LCR):** Requires banks to hold enough high-quality liquid assets (HQLA) to cover net cash outflows over a 30-day stress scenario.
        * **Net Stable Funding Ratio (NSFR):** A longer-term measure to ensure stable funding.



---

### 7.5 Pillar 1 Risk Charges (In-Depth)
#### Credit Risk (CRC)
Basel II/III offer three approaches for calculating Credit RWA:

1.  **Standardized Approach (SA):** Similar to Basel I, but uses external credit ratings (e.g., S&P, Moody's) to assign risk weights. For example, a AAA-rated corporate claim has a 20% RW, while a B-rated claim has a 150% RW.
2.  **Foundation IRB (FIRB):** Banks use their **internal models** to estimate the **Probability of Default (PD)** for each borrower. Other inputs (like LGD) are supplied by supervisors.
3.  **Advanced IRB (AIRB):** The most advanced method. Banks can use their own internal estimates for **PD, LGD, and Exposure at Default (EAD)**.

#### Market Risk (MRC)
Two approaches for calculating Market RWA:

1.  **Standardized Method:** A "building block" approach that sums capital charges for different risk types (interest rate, equity, FX, etc.). It ignores diversification benefits and is considered outdated.
2.  **Internal Models Approach (IMA):** Allows banks to use their own **VaR** models, subject to strict quantitative (e.g., 99% confidence, 10-day horizon, back-testing) and qualitative (e.g., independent risk control) standards.
    * **Revision (FRTB):** The framework is being revised ("Basel 2.5" / "Basel IV") to replace **VaR** with **Expected Shortfall (ES)**, as ES is better at capturing tail risk.




