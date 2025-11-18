# STAT4603 Toturial Note


## Example Class 1 (T1)

### Exercice 1

**Question:** An investment manager is given the task of beating a benchmark. Hence the risk should be measured in terms of
a) Loss relative to the initial investment
b) Loss relative to the expected portfolio value
c) Loss relative to the benchmark
d) Loss attributed to the benchmark

**Answer:** c. This is an example of risk measured in terms of deviations of the active portfolio relative to the benchmark. Answers a. and b. are incorrect because they refer to absolute risk. Answer d. is also incorrect because it refers to the absolute risk of the benchmark.

---

### Exercice 2

**Question:** Based on the risk assessment of the CRO, Bank United's CEO decided to make a large investment in a levered portfolio of CDOS. The CRO had estimated that the portfolio had a 1% chance of losing $1 billion or moreover one year, a loss that would make the bank insolvent. At the end of the first year the portfolio has lost $2 billion and the bank was closed by regulators. Which of the following statements is correct?
a) The outcome demonstrates a risk management failure because the bank did not eliminate the possibility of financial distress.
b) The outcome demonstrates a risk management failure because the fact that an extremely unlikely outcome occurred means that the probability of the outcome was poorly estimated.
c) The outcome demonstrates a risk management failure because the CRO failed to go to regulators to stop the shutdown.
d) Based on the information provided, one cannot determine whether it was a risk management failure.

**Answer:** d. It is the role of the CEO to decide on such investments, not the CRO. The CRO had correctly estimated that there was some chance of losing $1 billion or more. In addition, there is no information on the distribution beyond VAR. So, this could have been bad luck. A risk management failure could have occurred if the CRO had stated that this probability was zero.

---

### Exercice 3

**Question:** An analyst at CAPM Research Inc. is projecting a return of 21% on Portfolio A. The market risk premium is 11%, the volatility of the market portfolio is 14%, and the risk-free rate is 4.5%. Portfolio A has a beta of 1.5. According to the capital asset pricing model, which of the following statements is true?
a) The expected return of Portfolio A is greater than the expected return of the market portfolio.
b) The expected return of Portfolio A is less than the expected return of the market portfolio.
c) The return of Portfolio A has lower volatility than the market portfolio.
d) The expected return of Portfolio A is equal to the expected return of the market portfolio.

**Answer:** a. According to the CAPM, the required return on Portfolio A is $R_{F}+\beta[E(R_{M})-R_{F}]=4.5\%+1.5[11\%]=21\%$. Because the beta is greater than 1, it must be greater than the expected return on the market, which is 15.5%.

---

### Exercice 4

**Question:** Suppose Portfolio A has an expected return of 8%, volatility of 20%, and beta of 0.5. Suppose the market has an expected return of 10% and volatility of 25%. Finally, suppose the risk-free rate is 5%. What is Jensen's alpha for Portfolio A?
a) 10.0%
b) 1.0%
c) 0.5%
d) 15%

**Answer:** c. The CAPM return is $R_{F}+\beta[E(R_{M})-R_{F}]=5\%+0.5[10\%-5\%]=7.5\%$. Hence the alpha is 8% - 7.5% = 0.5%.

---

### Exercice 5

**Question:** Which of the following statements about the Sharpe ratio is false?
a) The Sharpe ratio considers both the systematic and unsystematic risks of a portfolio.
b) The Sharpe ratio is equal to the excess return of a portfolio over the risk-free rate divided by the total risk of the portfolio.
c) The Sharpe ratio cannot be used to evaluate relative performance of undiversified portfolios.
d) The Sharpe ratio is derived from the capital market line.

**Answer:** c. The SR considers total risk, which includes systematic and unsystematic risks, so a. and b. are correct statements. Similarly, the SR is derived from the CML. Finally, the SR can be used to evaluate undiversified portfolios, precisely because it includes idiosyncratic risk.

---

### Exercice 6

**Question:** A portfolio manager returns 10% with a volatility of 20%. The benchmark returns 8% with risk of 14%. The correlation between the two is 0.98. The risk-free rate is 3%. Which of the following statements is correct?
a) The portfolio has higher SR than the benchmark.
b) The portfolio has negative IR.
c) The IR is 0.35.
d) The IR is 0.29.

**Answer:** d. The Sharpe ratios of the portfolio and benchmark are $(10\%-3\%)/20\%=0.35$ and $(8\%-3\%)/14\%=0.36$ respectively. So the SR of the portfolio is lower than that of the benchmark. The TEV is the square root of $20\%^{2}+14\%^{2}-2\times0.98\times20\%\times14\%$ which is $\sqrt{0.00472}=6.87\%$. So, the IR of the portfolio is $(10\%-8\%)/6.87\%=0.29$.

---
---

## Example Class 2 (T2)

### Exercice 1

**Question:** Which of the following statements about trader limits are correct?
I. Stop loss limits are useful if markets are trending.
II. Exposure limits do not allow for diversification.
III. VAR limits are not susceptible to arbitrage.
IV. Stop loss limits are effective in preventing losses.
a) I and II
b) III and IV
c) I and III
d) II and IV

**Answer:** a. Stop loss limits cut down the positions after a loss is incurred, which is useful if markets are trending. Exposure limits do not allow for diversification, because correlations are not considered. VAR limits can be arbitraged. Stop loss limits are put in place after losses are incurred, so cannot prevent all losses. As a result, statements I. and II. are correct.

---

### Exercice 2

**Question:** The standard VAR calculation for extension to multiple periods also assumes that positions are fixed. If risk management enforces loss limits, the true VAR will be
a) The same
b) Greater than calculated
c) Less than calculated
d) Unable to be determined

**Answer:** c. The true VAR will be less than calculated. Loss limits cut down the positions as losses accumulate. This is similar to a long position in an option. Long positions in options have shortened left tails, and hence involve less risk than unprotected positions.

---

### Exercice 3

**Question:** The 10-Q report of ABC Bank states that the monthly VAR of ABC Bank is USD 10 million at the 95% confidence level. What is the proper interpretation of this statement?
a) If we collect 100 monthly gain/loss data of ABC Bank, we will always see five months with losses larger than $10 million.
b) There is a 95% probability that the bank will lose less than $10 million over a month.
c) There is a 5% probability that the bank will gain less than $10 million each month.
d) There is a 5% probability that the bank will lose less than $10 million over a month.

**Answer:** b. VAR is the worst loss such that there is a 95% probability that the losses will be less severe. Alternatively, there is a 5% probability that the losses will be worse. So b. is correct. Answer d. says "lose less" and therefore is incorrect.

---

### Exercice 4

**Question:** Given the following 30 ordered percentage returns of an asset, calculate the VAR and expected shortfall at a 90% confidence level: -16,-14,-10, -7,-7,-5,-4,-4,-4,-3,-1,-1, 0, 0, 0, 1, 2, 2, 4, 6, 7, 8, 9, 11, 12, 12, 14, 18, 21, 23.
a) VAR (90%) = 10, expected shortfall = 14
b) VAR (90%) = 10, expected shortfall = 15
c) VAR (90%) = 14, expected shortfall = 15
d) VAR (90%) = 18, expected shortfall = 22

**Answer:** b. The 10% lower cutoff point is the third lowest observation, which is VAR = 10. The expected shortfall is then the average of the observations in the tails, which is 15.

---

### Exercice 5

**Question:** Worse-than-VAR scenarios are defined as scenarios that lead to losses in the extreme left tail of the return distribution equal to or exceeding VAR at a given level of confidence. Which of the following statements is an accurate description of VAR?
a) VAR is the average of the worse-than-VAR scenario returns.
b) VAR is the standard deviation of the worse-than-VAR scenario returns.
c) VAR is the most pessimistic scenario return (maximum loss) from the worse-than-VAR scenarios.
d) VAR is the most optimistic scenario return (minimum loss) from the worse-than-VAR scenarios.

**Answer:** d. CVAR is the average of losses worse than VAR. Expressed in absolute value, VAR is lower than any other losses used for CVAR, so VAR must be the most optimistic loss.

---

### Exercice 6

**Question:** Assume that the P&L distribution of a liquid asset is i.i.d. normally distributed. The position has a one-day VAR at the 95% confidence level of $100,000. Estimate the 10-day VAR of the same position at the 99% confidence level.
a) $1,000,000
b) $450,000
c) $320,000
d) $220,000

**Answer:** b. We need to scale the VAR to a 99% level using $100,000 \times 2.326/1.645 = \$141,398$. Multiplying by $\sqrt{10}$ then gives $447,140. (This is closest to $450,000).

---

### Exercice 7

**Question:** Assume that portfolio daily returns are independent and identically normally distributed. Sam Neil, a new quantitative analyst, has been asked by the portfolio manager to calculate portfolio VARs over 10, 15, 20, and 25 days. The portfolio manager notices something amiss with Sam's calculations, displayed here. Which one of the following VARs on this portfolio is inconsistent with the others?
a) VAR(10-day) = USD 316M
b) VAR(15-day) = USD 465M
c) VAR(20-day) = USD 537M
d) VAR(25-day) = USD 600M

**Answer:** a. We compute the daily VAR by dividing each VAR by the square root of time. This gives $316/\sqrt{10}=100$ then 120, 120, and 120. So, answer a. is out of line.

---

### Exercice 8

**Question:** The 95%, one-day RiskMetrics VAR for a bank trading portfolio is $1,000,000. What is the approximate general market risk charge, as defined in 1996?
a) $3,000,000
b) $9,500,000
c) $4,200,000
d) $13,400,000

**Answer:** d. First, we have to convert the 95% VAR to a 99% measure. The GMRC is then $3 \times VAR \times \sqrt{10} = 3 \times \$1,000,000(2.33/1.65) \times \sqrt{10} = \$13,396,000$.

---

### Exercice 9

**Question:** Which of the following statements about stress testing are true?
I. Stress testing can complement VAR estimation in helping risk managers identify crucial vulnerabilities in a portfolio.
II. Stress testing allows users to include scenarios that did not occur in the lookback horizon of the VAR data but are nonetheless possible.
III. A drawback of stress testing is that it is highly subjective.
IV. The inclusion of a large number of scenarios helps management better understand the risk exposure of a portfolio.
a) I and II only.
b) III and IV only.
c) I, II and III only.
d) I, II, III and IV.

**Answer:** c. All the statements are correct except IV., because too many scenarios will make it more difficult to interpret the risk exposure.

---

### Exercice 10

**Question:** Which of the following is true about stress testing?
a) It is used to evaluate the potential impact on portfolio values of unlikely, although plausible, events or movements in a set of financial variables.
b) It is a risk management tool that directly compares predicted results to observed actual results. Predicted values are also compared with historical data.
c) Both a) and b) are true.
d) None of the above are true.

**Answer:** a. Stress testing is indeed used to evaluate the effect of extreme events. Answer b. is about backtesting, not stress-testing.

---

### Exercice 11

**Question:** John Flag, the manager of a $150 million distressed bond portfolio, conducts stress tests on the portfolio. The portfolio's annualized return is 12%, with an annualized return volatility of 25%. ... If the portfolio would suffer a 4-sigma daily event, estimate the change in the value of this portfolio.
a) $9.48 million
b) $23.70 million
c) $37.50 million
d) $150 million

**Answer:** a. First, we transform the volatility into a daily measure, which is $25\%/\sqrt{252}=1.57\%$. Multiplying, we get $150 \times 1.57\% \times 4 = \$9.45$.

---

### Exercice 12

**Question:** Which of the following methodologies would be most appropriate for stress-testing your portfolio?
a) Delta-gamma valuation
b) Full revaluation
c) Marking to market
d) Delta-normal VAR

**Answer:** b. By definition, stress-testing involves large movements in the risk factors. This requires a full revaluation of the portfolio.

---
---

## Example Class 3 (T3)

### Exercice 1

**Question:** Which of the following is not a type of operational risk as defined by Basel II?
a) Human error and internal fraud
b) Destruction by fire or other external catastrophes
c) Damaged reputation due to a failed merger
d) Failure or breakdown in internal control processes

**Answer:** c. Damaged reputation due to a failed merger is a business risk. Also, reputational risk is not a type of operational loss.

---

### Exercice 2

**Question:** Which of these outcomes is not associated with an operational risk process?
a) The sale of call options is booked as a purchase.
b) A monthly volatility is inputted in a model that requires a daily volatility.
c) A loss is incurred on an option portfolio because ex post volatility exceeded expected volatility.
d) A volatility estimate is based on a time series that includes a price that exceeds the other prices by a factor of 100.

**Answer:** c. Choices a., b., and d. are operational losses. Answer c. is the result of a bet on volatility, which is market risk.

---

### Exercice 3

**Question:** All the following are operational risk loss events, except:
a) An individual shows up at a branch presenting a check written by a customer for an amount substantially exceeding the customer's low checking account balance...
b) A bank, acting as a trustee for a loan pool, receives less than the projected funds due to delayed repayment of certain loans.
c) During an adverse market movement, the computer network system becomes overwhelmed...
d) A loan officer inaccurately enters client financial information into the bank's proprietary credit risk model.

**Answer:** b. Statement a. represents external fraud, which is included in operational risk. Statement c. represents a systems failure. Statement d. is a failure in internal processes. (Answer b is credit risk).

---

### Exercice 4

**Question:** The risk of the occurrence of a significant difference between the mark-to-model value of a complex instrument and the price at which the same instrument is revealed to have traded in the market is referred to as:
a) Liquidity risk
b) Dynamic risk
c) Model risk
d) Mark-to-market risk

**Answer:** c. This is a situation where the model price is significantly different from the market price, which is model risk.

---

### Exercice 5

**Question:** Gerard Kuper is modeling the number of operational risk loss events... He expects the number of operational risk loss events for the year to be relatively small. Which type of distribution is he least likely to use?
a) Normal distribution
b) Binomial distribution
c) Negative binomial distribution
d) Poisson distribution

**Answer:** a. The last three distributions require the number n to be positive, which is not the case for the normal distribution.

---

### Exercice 6

**Question:** The severity distribution of operational losses usually has the following shape:
a) Symmetrical with short tails
b) Long-tailed to the right
c) Uniform
d) Symmetrical with long tails

**Answer:** b. Loss severity distributions are bounded by zero but should include very large losses. So, they are asymmetrical with long right tails.

---

### Exercice 7

**Question:** ...external loss data is inherently biased. Which of the following is not typically associated with external data?
a) Data capture bias
b) Scale bias
c) Truncation bias
d) Survivorship bias

**Answer:** d. Internal data certainly has a problem of survivorship bias because a bank where employees compute the operational risk distribution is still alive.

---

### Exercice 8

**Question:** Capital is used to protect the bank from which of the following risks?
a) Risks with an extreme financial impact
b) High-frequency, low-loss events
c) Low-frequency risks with significant financial impact
d) High-frequency uncorrelated events

**Answer:** c. Capital is supposed to absorb risks that have significant financial impact on the firm. Risks with extreme financial impact, such as systemic risk, cannot be absorbed by capital alone. Low-loss events are unimportant. Uncorrelated events tend to diversify.

---

### Exercice 9

**Question:** Which of these terms is used in the insurance industry to refer to the effect of a reduction in the control of losses by an individual who is insured because of the protection provided by insurance?
a) Control trap
b) Moral hazard
c) Adverse selection
d) Control hazard

**Answer:** b. Moral hazard arises when insured individuals have less incentive to control their losses because they are insured.

---

### Exercice 10

**Question:** Which of the following options does not describe a problem faced by banks when purchasing insurance as a hedge against operational risk?
a) The fact that the loss reimbursement period can take several years
b) The credit rating of insurers
c) The different perspective of operational risk between banks and insurers
d) Not having an operational VAR

**Answer:** d. Answers a., b., and c. describe problems arising from the purchase of insurance against operational risk. This is irrespective of whether the bank has an operational VAR model.

---

### Exercice 11

**Question:** Insurance is an effective tool to transfer which of type of operational risk?
a) High frequency, low severity
b) Low frequency, high severity
c) Operational losses whose magnitude is affected by the actions of the company
d) Operational losses for which insurance companies only sell policies with low limits

**Answer:** b. The purpose of insurance is to reimburse large losses, or operational risk events with high severity.

---

### Exercice 12

**Question:** Which of the following statements are valid about hedging operational risk?
I. A primary disadvantage of insurance as an operational risk management tool is the limitation of policy coverage.
II. If an operational risk hedge works properly, a firm will avoid damage to its reputation from a high-severity operational risk event.
III. While all insurance contracts suffer from the problem of moral hazard, deductibles help reduce this problem.
IV. Catastrophe (cat) bonds allow a firm to hedge operational risks associated with natural disasters.
a) I, III and IV
b) I, II and IV
c) II and III
d) III and IV

**Answer:** a. All the statements are valid, except for II. Even if a firm implements a hedge or purchases insurance, the news of a large operational loss will still damage its reputation.

---

### Exercice 13

**Question:** The following statements concern differences between market and operational risk VAR models. Which of the following statements is false?
a) Market risk models are primarily driven by historical data, whereas operational risk models are more flexible in this regard.
b) Market risk models typically define VAR as a specific quantile of the loss distribution, whereas operational risk models are more flexible in this regard.
c) Backtesting is generally a more useful form of validation for market risk models than for operational risk models.
d) The time horizon over which VAR is evaluated differs between market and operational risk models.

**Answer:** b. Statement a. is true. Backtesting is more difficult for operational risk models, so c. is true. VAR is usually evaluated over shorter horizons, so d. is true. Statement b. is false because both market and operational risk models use a quantile of the distribution.

---

### Exercice 14

**Question:** Which of the following approaches for calculating operational risk capital charges leads to a higher capital charge for a given accounting income as risk increases?
a) The basic indicator approach
b) The standardized approach
c) The advanced measurement approach
d) All of the above

**Answer:** c. The basic indicator approach uses a factor of 15%. The standardized approach uses a fixed factor... so is not risk sensitive. The AMA is the most risk-sensitive method.

---

### Exercice 15

**Question:** Which of the following statements about its methodology for calculating an operational risk capital charge in Basel II is correct?
a) The basic indicator approach is suitable for institutions with sophisticated operational risk profiles.
b) Under the standardized approach, the capital requirement is measured for each of the business lines.
c) Advanced measurement approaches will not allow an institution to adopt its own method of assessment of operational risk.
d) The AMA is less risk sensitive than the standardized approach.

**Answer:** b. The BIA is suitable for banks with basic risk profiles, so answer a. is incorrect. The AMA is an internal model, so answer c. is incorrect. The AMA is more risk sensitive than the standardized approach, so answer d. is incorrect.

---

### Exercice 16

**Question:** Which of the following statements regarding Basel II nonadvanced approaches is incorrect?
a) The standardized approach makes it advantageous for a bank to book losses early if doing so reduces this year's gross income sufficiently to make it negative.
b) Corporate finance, trading and sales, and payment and settlement are the business lines with the highest regulatory capital requirements.
c) The standardized approach divides the bank into business lines and uses data from the last three years of a business line's gross income and a beta factor to obtain the regulatory capital for that business line.
d) The standardized approach uses data from the last three years of gross income to obtain a bank's operational risk capital charge.

**Answer:** a. Statement a. is incorrect because only positive income is considered. Statement b. is correct. Statements c. and d. are correct as well.

---
---

## Example Class 4 (T4)

### Exercice 1

**Question:** Which of the following statements regarding liquidity risk is correct?
a) Asset liquidity risk arises when a financial institution cannot meet payment obligations.
b) Flight to quality is usually reflected in a decrease in the yield spread between corporate and government issues.
c) Yield spread between on-the-run and off-the-run securities mainly captures the liquidity premium, and not the market and credit risk premium.
d) Funding liquidity risk can be managed by setting limits on certain asset markets or products and by means of diversification.

**Answer:** c. The yield spread between on-the-run and off-the-run securities reflects a liquidity premium because the bonds are otherwise nearly identical. In answers a. and d., asset and funding risk should be interchanged. For b., a flight to quality increases the yield spread.

---

### Exercice 2

**Question:** The following statements compare a highly liquid asset against an (otherwise similar) illiquid asset. Which statement is most likely to be false?
a) It is possible to trade a larger quantity of the liquid asset without affecting the price.
b) The liquid asset has a smaller bid-ask spread.
c) The liquid asset has higher price volatility since it trades more often.
d) The liquid asset has higher trading volume.

**Answer:** c. The liquid stock typically has higher trading volumes and smaller bid-ask spreads, so b. and d. are true. It also has greater depth, meaning that large quantities can be traded without affecting prices too much, so a. is true. As a result, the remaining answer, c. must be wrong. There is no necessary relationship between trading activity and volatility.

---

### Exercice 3

**Question:** A mutual fund investing in common stocks has adopted a liquidity risk measure limiting each of its holdings to a maximum of 30% of its 30-day average value traded. If the fund size is USD 3 billion, what is the maximum weight that the fund can hold in a stock with a 30-day average value traded of USD 2.4 million?
a) 24.00%
b) 0.08%
c) 0.024%
d) 80.0%

**Answer:** c. The maximum weight w is given by $3,000 \times w = 30\% \times \$2.4$, or $w=0.024\%$.

---

### Exercice 4

**Question:** In a market crash, which the following are usually true?
I. Fixed-income portfolios hedged with short Treasury bonds and futures lose less than those hedged with interest rate swaps given equivalent durations.
II. Bid-offer spreads widen because of lower liquidity.
III. The spreads between off-the-run bonds and benchmark issues widen.
a) I, II and III
b) II and III
c) I and III
d) None of the above

**Answer:** b. In a crash, bid-offer spreads widen, as do liquidity spreads. Statement I. is incorrect because Treasuries usually rally more than swaps, which leads to greater losses for a portfolio short Treasuries than swaps.

---

### Exercice 5

**Question:** You are holding 100 Wheelbarrow Company shares with a current price of $50. The daily mean and volatility of the stock return is 1% and 2%, respectively. ... The bid-ask spread of the stock varies over time. The daily mean and volatility of the spread are 0.5% and 1%, respectively. Both the return and spread are normally distributed. Calculate the daily liquidity-adjusted VAR (LVAR) at a 99% confidence level.
a) USD 254
b) USD 229
c) USD 325
d) USD 275

**Answer:** a. The regular VAR... is $VAR = W(\alpha\sigma - \mu) = \$5,000(2.33 \times 2\% - 1\%) = \$183$. To this must be added $L_{2} = 0.5W(S + \alpha'\sigma_{S}) = 0.5 \times \$5,000(0.5\% + 2.33 \times 1\%) = \$70.75$. for a total of $254.

---

### Exercice 6

**Question:** You are a manager... analyzing a 1,000-share position in... stock BNA, which has a current stock price of USD 72 (expressed as the midpoint of the current bid-ask spread). Daily return for BNA has an estimated volatility of 1.24%. The average bid-ask spread is USD 0.16. Assuming returns of BNA are normally distributed, what is the estimated liquidity-adjusted daily 95% VAR, using the constant spread approach?
a) USD 1,389
b) USD 1,469
c) USD 1,549
d) USD 1,629

**Answer:** c. Conventional VAR is $\$72 \times 1,000 \times 1.24\% \times 1.645 = \$1,469$. The spread effect is $0.5 \times \$0.16 \times 1,000 = \$80$. for a total of $1,549.

---

### Exercice 7

**Question:** ...the TED spread increased sharply. Which of the following statements best describes the change in your situation?
a) An increase in the TED spread indicates that the Federal Reserve will push interest rates up...
b) An increase in the TED spread indicates a bigger gap between the fed funds rate and treasuries...
c) An increase in the TED spread could indicate greater concerns about bank solvency, so that you should review your counterparty exposures...
d) An increase in the TED spread could indicate more willingness of banks to lend...

**Answer:** c. Statement a. is not correct.... Statement b. is not correct because the fed funds rate is for collateralized loans, whereas Eurodollar rates are for uncollateralized deposits. Statement d. is incorrect because a wider TED spread means that the cost of bank borrowing goes up.

---

### Exercice 8

**Question:** ...how market liquidity is affected by shocks to the financial system. Which of the following observations made in the memo is incorrect?
a) In periods of acute market stress, market liquidity typically increases in the most liquid markets, creating a self-correcting loop...
b) Evaporation of market liquidity is an important factor in determining... financial shocks...
c) Market shocks may not be reflected in mark-to-market portfolio values immediately for portfolios with illiquid assets.
d) The impact of a market shock on the liquidity of a specific asset depends on the characteristics of the investors who own the asset.

**Answer:** a. Statement b. is correct. Statement c. correctly states that the prices of illiquid assets reflect a delayed reaction to events. Statement d. explains that asset liquidity depends on investor positions, which is correct.

---

### Exercice 9

**Question:** ...which of the following are early warning indicators of a potential liquidity problem?
I. Rapid asset growth, especially when funded with potentially volatile liabilities
II. Growing concentrations in assets or liabilities
III. An increase of the weighted average maturity of liabilities
IV. Reduction in the frequency of positions approaching or breaching internal or regulatory limits
V. Narrowing debt or credit default swap spreads
VI. Counterparties that request additional collateral for credit exposures
VII. Increasing redemptions of CDs before maturity
a) I, II, VI and VII
b) I, III, V and VI
c) II, IV, V, and VII
d) I, V, VI and VII

**Answer:** a. Statement I. is correct. Statement II. is also a problem. Statement III. is not a correct answer, because longer liabilities reduce the probability of a near-term funding problem. Statement IV. is not a correct answer. Statement V. is not a correct answer, because a problem would arise from widening, not narrowing spreads. Statement VI. is correct because collateral demands create a claim on liquidity. Statement VII. is correct because this requires cash for repayment.

---
---

## Tutorial 5 (T5)

### Q1

**Question:** An asset is quoted bid 50, offer 55. What does this mean? What is the proportional bid-offer spread?

**Answer:**
* **Meaning:** The "offer 55" is the price you can pay to buy the asset. The "bid 50" is the amount you can receive from selling the asset.
* **Proportional Bid-Offer Spread:**
    1.  **Mid-market price:** (ask price + bid price) / 2 = (55 + 50) / 2 = 52.5
    2.  **Proportional spread:** (ask price - bid price) / mid-market price = (55 - 50) / 52.5 = 0.0952

---

### Q2

**Question:**
a) Suppose that an investor has shorted shares worth $5,000 of Company A and bought shares worth $3,000 of Company B. The proportional bid-offer spread for Company A is 0.01 and the proportional bid-offer spread for Company B is 0.02. What does it cost the investor to unwind the portfolio?

b) Suppose now that the bid-offer spreads for the two companies are normally distributed. For Company A the bid-offer spread has a mean of 0.01 and a standard deviation of 0.01. For Company B the bid-offer spread has a mean of 0.02 and a standard deviation of 0.03. What is the cost of unwinding that the investor is 95% confident will not be exceeded?

**Answer:**
**a) Cost of liquidation in normal market:**
* The formula is $\sum \frac{s_{i}\alpha_{i}}{2}$, where $\alpha_{i}$ is the dollar value at mid-market price.
* Cost for A (b/a spread): 0.01 * $5,000 = $50
* Cost for B (b/a spread): 0.02 * $3,000 = $60
* Total Cost of unwinding: ($50 + $60) / 2 = $55

**b) Cost of liquidation in stressed market (95% confidence):**
* The formula is $\sum \frac{(\mu_{i}+\lambda\sigma_{i})\alpha_{i}}{2}$. For 95% confidence, $\lambda = 1.645$.
* Cost for A: $5,000 \times (0.01 + 1.645 \times 0.01) = \$132.25$
* Cost for B: $3,000 \times (0.02 + 1.645 \times 0.03) = \$208.05$
* Total Cost of unwinding: ($132.25 + $208.05) / 2 = $170.15

---

### Q3

**Question:**
1. A hedge fund has a position in 1 million shares of a stock whose midprice is $100. The bid-ask spread is $0.40, up to a volume of 100,000. Beyond that, prices fall by $0.50 per share for every 100,000 shares transacted in one day. Compute the loss from the midprice if the entire position is liquidated over 1 day.
2. Repeat with two other scenarios:
   (a) The sale is spread uniformly over 5 days.
   (b) The sale is spread uniformly over 10 days.

**Answer:**
**1. Liquidation in 1 day:**
* **Spread Cost:** This is incurred on all shares. Cost = 0.5 * (bid-ask spread) * (total shares) = 0.5 * $0.40 * 1,000,000 = $200,000.
* **Price Impact Cost (Additional Cost):** This applies to shares sold beyond the 100,000 NMS limit.
    * Shares beyond NMS: 1,000,000 - 100,000 = 900,000 shares.
    * Price drop per share: $0.50 \times \frac{1,000,000 - 100,000}{100,000} = \$0.50 \times 9 = \$4.50$ per share.
    * Additional Cost: $4.50 * 900,000 = $4,050,000.
* **Total Cost:** $200,000 (Spread) + $4,050,000 (Impact) = $4,250,000.

**2. (a) Liquidation over 5 days:**
* **Shares per day:** 1,000,000 / 5 = 200,000 shares.
* **Spread Cost (Total):** $200,000 (This is incurred on the entire portfolio).
* **Price Impact Cost (per day):**
    * Shares beyond NMS (per day): 200,000 - 100,000 = 100,000 shares.
    * Price impact per share (on these shares): $0.50 \times \frac{200,000 - 100,000}{100,000} = \$0.50 \times 1 = \$0.50$ per share.
    * Additional cost (per day): $0.50 * 100,000 = $50,000.
    * Total Additional Cost (over 5 days): 5 days * $50,000 = $250,000.
* **Total Cost:** $200,000 (Spread) + $250,000 (Impact) = $450,000.

**2. (b) Liquidation over 10 days:**
* **Shares per day:** 1,000,000 / 10 = 100,000 shares.
* **Price Impact Cost:** Since the daily sale (100,000) is within the NMS limit (100,000), there is no additional price impact cost.
* **Total Cost:** The only cost is the spread cost, which is $200,000.

## Example Class 6 (T6)

### Exercice 1

**Question:** Which of these statements about economic and regulatory capital are valid?
I. Regulatory capital seeks soundness and stability in the banking system by ensuring that there is enough capital in the banking system.
II. Economic capital is designed to keep a financial institution solvent at a specified confidence level.
III. For an individual bank, economic capital is always less than regulatory capital.
IV. The determination of economic capital, and its allocation to the various business units, is a strategic decision process that affects the risk/return performance of the business units and the bank as a whole.
a) II and IV only
b) I, II, III and IV
c) I, II and IV
d) I and IV only

**Answer:** c. All the statements are correct, except c., that economic capital must always be less than regulatory capital. This is too broad a statement. The two measures are not necessarily related, even though this is the goal of having more risk-sensitive capital requirements.

---

### Exercice 2

**Question:** Tower Bank approaches economic capital and risk aggregation by first estimating the stand-alone economic capital for individual risk factors. In a second step, the bank aggregates risks based on the relative amounts of economie capital allocated to these risks, taking into account the correlations between risk factors. Which of the following variables is not a primary driver of the diversification benefit that accrues from aggregation?
a) The number of risk positions
b) The size of the portfolio
c) The concentration of those risk positions, or their relative weights in a portfolio
d) The correlation between the positions

**Answer:** b. A portfolio is generally more diversified when it has many positions, which are not too large, and with low correlations. Hence answers a., c., and d. involve drivers of diversification. In contrast, risk measures are homogeneous with the size of the portfolio. Doubling all the positions will double the risk of the portfolio.

---

### Exercice 3

**Question:** Consider a bank that wants to have an amount of capital so that it can absorb unexpected losses corresponding to a firmwide VAR at the 1% level. It measures firmwide VAR by adding up the VARS for market risk, operational risk, and credit risk. There is a risk that the bank has too little capital because
a) It does not take into account the correlations among risks.
b) It ignores risks that are not market, operational, or credit risks.
c) It mistakenly uses VAR to measure operational risk because operational risks that matter are rare events.
d) It is meaningless to add VARS.

**Answer:** b. VAR can be added across different types of risk, but this will provide a conservative estimate of capital as diversification effects are ignored. So answer a. would be for too much capital. Answer c. is not correct because rare events can be factored into operational VAR. Most likely, the bank may have too little capital for other types of risk than those measured by these three categories.

---

### Exercice 4

**Question:** Large banks typically allocate risk capital for credit, operational, and market/ALM risks. Which of the following statements ranks the typical amount of risk capital allocated to these different risks correctly?
a) Market/ALM risk requires more risk capital than credit risk.
b) Credit risk requires more risk capital than market/ALM risk, which requires more risk capital than operational risk.
c) Market/ALM risk requires more risk capital than operational risk but less than credit risk.
d) Credit risk requires more risk capital than operational risk, which requires more risk capital than market/ALM risk.

**Answer:** d. For most global banks, the order of importance is, first, credit risk, then operational risk, then market/ALM risk.

---

### Exercice 5

**Question:** Counterparty A is an American company with manufacturing operations in Indonesia and its main customers in the United States, while counterparty B is an American company that manufactures its goods domestically and exports solely to Indonesia. Which one of the following transactions with either counterparty will be a wrong-way exposure for a bank?
a) A five-year plain-vanilla IDR/USD cross-currency swap between the bank and counterparty A where the bank is USD interest rate receiver
b) A five-year plain-vanilla IDR/USD currency option sold by the bank to counterparty A for it to buy IDR at a certain rate
c) A five-year plain-vanilla IDR/USD cross-currency swap between the bank and counterparty B where the bank is USD interest rate receiver
d) A five-year plain-vanilla IDR/USD currency option bought by the bank from counterparty B for the bank to buy IDR at a certain rate

**Answer:** c. This is an example of a wrong-way exposure... If the IDR depreciates... counterparty B, because its dollar revenues will decrease. Under c., the company pays USD and receives IDR. This transaction will create a loss if the IDR depreciates. In this situation, counterparty B will lose money as well on its exports. Hence, this is a wrong-way trade.

---

### Exercice 6

**Question:** Your bank calculates a one-day 95% VAR for market risk, a one-year 99% VAR for operational risk, and a one-year 99% VAR for credit risk. The measures are $100 million, $500 million, and $1 billion, respectively. Operational risk is degined to include all risks that are not market risks and credit risks, and these three categories are mutually uncorrelated... Your boss wants your best estimate of a firmwide VAR at the 1% level. Among the following choices, your best estimate is:
a) $1.7 billion
b) $1.94 billion
c) $2.50 billion
d) It is impossible to aggregate risks with different distributions having only this information.

**Answer:** c. First, we convert the daily VAR at the 95% level to the same parameters as the other. With the normality assumption, this is $VAR_{MKT}=\$100\times(2.326/1.645)\sqrt{252}=\$2,245.$ We then combine the three VARs by taking the square root of the sum of squares, which gives $VAR=\sqrt{\$2,245^{2}+\$500^{2}+\$1,000^{2}=\$2,458.}$ (Note: The solution file's calculation $2,245 \text{ million} + 500 \text{ million} + 1,000 \text{ million}$ seems to have a typo, as $2.245B + 0.5B + 1B$ aggregated this way is $2.50B$. The numbers in the calculation ($2,245$, $500$, $1000$) seem to be in millions, resulting in $2,458$ million, or $2.458$ billion, which rounds to $2.50$ billion).

---

### Exercice 7

**Question:** The failure of Barings Bank is a typical example of a lack in control pertaining to which one of the following risks?
a) Liquidity risk
b) Credit risk
c) Operational risk
d) Foreign exchange risk

**Answer:** c. The Barings failure falls in the category of operational risk because of a breakdown in procedures. The trader, Nick Leeson, had control of the back office.

---

### Exercice 8

**Question:** ...rigorous stress-testing should be an important component of risk measurement and management. To improve the value of stress-testing exercises, firms should consider all of the following except:
a) Asking risk managers to define and clearly express firm loss tolerance levels
b) Identifying a range of scenarios that could produce portfolio losses
c) Ranking the stress scenarios by level of potential adverse impact and assessing relative probabilities for scenarios
d) Ensuring that stress tests are plausible and consistent with the existing risk model framework

**Answer:** a. Business managers or the board of directors should define the risk tolerance, not risk managers.

---

### Exercice 9

**Question:** When would it be prudent for a trader to direct accounting entries?
a) Never
b) When senior management of the firm and the board of directors are aware and have approved the practice on an exception basis
c) When audit controls are such that the entries are reviewed on a regular basis to ensure detection of irregularities
d) Solely during such times as staffing turnover requires the trader to backfill until additional personnel can be hired and trained

**Answer:** a. As one risk manager has said, this is one of the few instances where never means absolutely never. Allowing traders to tabulate their own profits and losses is a recipe for disaster.

---

### Exercice 10

**Question:** Which of the following is not a proper practice of risk management and control for a financial institution with assets in excess of $100 million?
a) A firm's sole mechanism to monitor the implementation of the control policies defined by the board is an external audit firm.
b) A subcommittee of the board is responsible for the approval of risk limits, risk management policies, and delegation of exceptional approval authorities.
c) Senior management is responsible for the day-to-day oversight of the firm's activities, implementing appropriate risk management and control policies, and monitoring the risks and exposures of the firm.
d) Senior management is responsible for establishing written documentation about control procedures at each level of the control hierarchy.

**Answer:** a. Control policies also need to be verified by an internal audit function.

---

### Exercice 11

**Question:** The following is not a problem of having one employee perform trading functions and back-office functions.
a) The employee gets paid more because she performs two functions.
b) The employee can hide trading mistakes when processing the trades.
c) The employee can hide the size of her book.
d) The employee's firm may not know its true exposure.

**Answer:** a. Answers b., c., and d. all can lead to a situation where the trader loses money and hides the losses. Answer a. is not a problem per se.

---

### Exercice 12

**Question:** Which of the following strategies can contribute to minimizing operational risk?
I. Individuals responsible for committing to transactions should perform clearance and accounting functions.
II. To value current positions, price information should be obtained from external sources.
III. Compensation schemes for traders should be directly linked to calendar revenues.
IV. Trade tickets need to be confirmed with the counterparty.
a) I and II
b) II and IV
c) III and IV
d) I, II and III

**Answer:** b. Answer I. violates the principle of separation of functions. Answer III. may create problems of traders taking too much risk. Answer II. advises the use of external sources for valuing positions. (Answer IV, confirmation, is also a standard control).

---

### Exercice 13

**Question:** To control risk taking by traders, your bank links trader compensation with their compliance with imposed VAR limits on their trading books. Why should your bank be careful in tying compensation to the VAR of each trader?
a) It encourages traders to select positions with high estimated risks, which leads to an underestimation of the VAR limits.
b) It encourages traders to select positions with high estimated risks, which leads to an overestimation of the VAR limits.
c) It encourages traders to select positions with low estimated risks, which leads to an underestimation of the VAR limits.
d) It encourages traders to select positions with low estimated risks, which leads to an overestimation of the VAR limits.

**Answer:** c. Traders may engage in VAR arbitrage, trying to exploit weaknesses in VAR measures. With a VAR limit, they may seek positions that have low measured VAR, in which case the VAR limits will be less effective.

---

### Exercice 14

**Question:** A risk manager for ABC Bank has compiled the following data regarding a bond trader and an equity trader... Calculate the risk-adjusted performance measure (RAPM) for the bond trader.
(Data: Bond Trader: After-Tax Profit $8M, Net Book Market Value $120M, Weekly Volatility 1.10%, Tax Rate 40%)
a) 25.24%
b) 36.08%
c) 60.15%
d) 84.92%

**Answer:** c. The 99% VAR is $2.33\times1.10\%\times\sqrt{52}\times(1-40\%)\times\$120=\$13.3$ million. Hence $RAPM=8/13.3$ = 60.1%. (Note: The calculation appears to be using (1-Tax Rate) * Book Value, which is not standard. However, following the solution's logic: $VAR = 2.33 \times 0.011 \times \sqrt{52} \times 0.60 \times 120 = 13.32$. $RAPM = \text{Profit} / VAR = 8 / 13.32 \approx 0.6015$ or 60.15%).

---

### Exercice 15

**Question:** Continuing with the same ABC Bank data, which of the following statements is correct in relation to the equity trader?
I. The equity trader has an annual, after-tax VAR at a 99% confidence level of USD 33.2 million.
II. In comparing the RAROC for both traders, the equity trader is performing better than the bond trader.
(Data: Equity Trader: After-Tax Profit $18M, Net Book Market Value $180M, Weekly Volatility 1.94%, Tax Rate 40%)
a) I only
b) II only
c) Both
d) Neither

**Answer:** d. The equity trader's VAR is $2.33\times1.94\%\times\sqrt{52}\times(1-40\%)\times\$180=\$35.2$ million, so statement I. is incorrect. The RAPM is 18 / 35.2, or 51.1%, which is worse than that of the bond trader (60.1%), so statement II. is incorrect as well.

---

### Exercice 16

**Question:** The bank you work for has a RAROC model... You are asked to estimate the RAROC of its $500 million loan business. The average interest rate is 10%. All loans have the same probability of default of 2% with a loss given default of 50%. Operating costs are $10 million. The funding cost of the business is $30 million. RAROC is estimated using a credit VAR for loan businesses, in this case 7.5%. The economic capital is invested and earns 6%. The RAROC is:
a) 19.33%
b) 46.00%
c) 32.67%
d) 13.33%

**Answer:** a. First, we compute the numerator. The net interest is, after expected losses, $\$500\times[10\%-2\%(1-50\%)]=\$45$. Next, we compute economic capital, or $\$500\times7.5\%=\$37.5$. To revenues, we then add the return on economic capital, or $\$37.5\times6\%=\$2.25$. From this, we deduct operating and funding costs, which gives $\$47.25-10-30=\$7.25$. Finally, we divide by $37.5 and get 19.33%.