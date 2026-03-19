# STAT4608 Formula Sheet

### 1. Asset Returns
Understanding basic return calculations is fundamental before assessing market risk.

* **Simple Return ($k$-period):** The compounded simple return over $k$ periods.
    $$R_{t}[k]=\prod_{j=0}^{k-1}(1+R_{t-j})-1$$
    * **Example:** For daily returns of -0.0303, -0.0116, and 0.0239, the 3-day simple return is $(1-0.0303)(1-0.0116)(1+0.0239)-1 = -0.0186$.
* **Log Return ($k$-period):** The natural logarithm of the $k$-period simple return multiplier.
    $$r_{t}[k]=\ln(1+R_{t}[k])$$
    * **Example:** Using the simple return above, the 3-day log return is $\ln(0.981358) = -0.0188$.

---

### 2. Value at Risk (VaR)
VaR measures the maximum expected loss at a given significance level over a target horizon.

**General Formulas:**
* **Relative VaR:** Measures loss relative to the expected future value.
    $$VaR_{\alpha}(\mu)=E(V)-V^{*}$$
* **Absolute VaR:** Measures loss relative to the initial investment value.
    $$VaR_{\alpha}(0)=V_{0}-V^{*}$$

**Non-Parametric Approach (Historical Simulation):**
* **Explanation:** Uses actual sorted historical returns. If the target index is not an integer, linear interpolation is used between the adjacent ordered returns.
* **Example:** For 252 days at a 98% confidence level, the index is $252 \times 0.02 = 5.04$. Interpolating between the 5th (-2.5%) and 6th (-2.4%) lowest returns gives a cutoff $R^{*} = (-2.5)\times 0.96 + (-2.4)\times 0.04 = -2.496\%$. With an initial value of $100,000, the absolute VaR is $-100,000 \times (-0.02496) = \$2,496$.

**Parametric Approach (Normal Distribution):**
* **Explanation:** Assumes returns follow a normal distribution.
* **Relative VaR Formula:** $$VaR(\mu)=V_{0}Z_{\alpha}S$$
* **Example:** With a mean of 0.04%, standard deviation of 0.5%, $V_0=100,000$, and $Z_{0.02}=2.054$, the relative VaR is $100,000 \times 2.054 \times 0.005 = \$1,027$. The absolute VaR is $1,027 - (100,000 \times 0.0004) = \$987$.

---

### 3. Expected Shortfall (ES)
ES measures the expected loss given that the loss has exceeded the VaR threshold.
* **General Formula:** $$ES=E(L|L>VaR)$$

**Non-Parametric Approach:**
* **Explanation:** The sample mean of the observed losses that exceed the VaR.
    $$\hat{ES}=\frac{1}{m}\sum_{j=1}^{m}L_{i_{j}}$$
* **Example:** If 5 returns exceed the VaR threshold, their average is $\frac{-7.2-5.3-3.0-2.6-2.5}{5} = -4.12\%$. The ES is $100,000 \times 0.0412 = \$4,120$.

**Parametric Approach (Normal Model):**
* **Formula:** $$\hat{ES}=\frac{\hat{\sigma}_{W}\phi(\hat{q})}{\alpha}-\hat{\mu}_{W}$$

---

### 4. Time Scaling (Under EMH)
Under the Efficient Market Hypothesis (EMH), returns are assumed to be independent and identically distributed (i.i.d.).
* **Explanation:** To scale from a 1-day horizon to a $T$-day horizon, scale the mean by $T$ and the standard deviation by $\sqrt{T}$.
* **Example:** A daily mean of 0.04% and volatility of 0.5% scale to a 10-day mean of $10 \times 0.04\% = 0.4\%$ and a 10-day volatility of $\sqrt{10} \times 0.5\% \approx 1.5811\%$. The 10-day 99% relative VaR becomes $100,000 \times 2.326 \times 0.015811 = \$3,677.64$.

---

### 5. Portfolio Risk
Evaluating the risk of multiple assets combined.

* **Portfolio Variance:**
    $$\sigma_{v}^{2}=x^{\prime}\Sigma x$$
    * **Example (Two Assets):** $\sigma_{v}^{2}=x_{A}^{2}\sigma_{A}^{2}+x_{B}^{2}\sigma_{B}^{2}+2x_{A}x_{B}\sigma_{AB}$. For a portfolio with capital allocations of 1,000,000 and 2,000,000, this results in $160,000,000 + 360,000,000 - 192,000,000 = 328,000,000$.
* **Diversified Portfolio VaR:**
    $$VaR_{p}=Z_{\alpha}\sqrt{x^{\prime}\Sigma x}$$
    * **Example:** $2.326 \times \sqrt{328,000,000} = \$42,125.65$.
* **Undiversified VaR:** The simple sum of individual VaRs.
    $$\sum_{i=1}^{N}VaR_{i}=\sum_{i=1}^{N}Z_{\alpha}\sigma_{i}|w_{i}|V_{0}$$
    * **Example:** $\$29,421.83 + \$44,132.75 = \$73,554.58$.
* **Marginal VaR:** Measures risk contribution per unit of capital.
    $$\Delta VaR=VaR_{p}\frac{\Sigma x}{x^{\prime}\Sigma x}$$
    * **Example:** For Stock A, $42,125.65 \times \frac{64}{328,000,000} \approx 0.008220$.
* **Component VaR:** The total risk contribution of a specific asset to the portfolio.
    $$CVaR_{i}=(\Delta VaR_{i})\times x_{i}$$
    * **Example:** $0.008220 \times 1,000,000 = \$8,220$.

---

To understand how to calculate $\Sigma x$ and $x^\prime\Sigma x$, it helps to break down the linear algebra into simple, step-by-step arithmetic. In the context of portfolio risk, these calculations are used to find the total portfolio variance and the marginal risk contributions of individual assets.



Here is the step-by-step explanation based on the two-asset portfolio example provided in your document (Stock A and Stock B).

### 1. Define the Variables
First, identify your capital allocation vector ($x$) and your variance-covariance matrix ($\Sigma$).

* **$x$ (Capital Allocation Vector):** This is a column matrix representing the dollar amount invested in each asset.
    $$x = \begin{pmatrix} x_{A} \\ x_{B} \end{pmatrix} = \begin{pmatrix} 1,000,000 \\ 2,000,000 \end{pmatrix}$$

* **$\Sigma$ (Variance-Covariance Matrix):** This matrix holds the daily variances ($\sigma^2$) on the diagonal and the covariance ($\sigma_{AB}$) on the off-diagonal.
    $$\Sigma = \begin{pmatrix} \sigma_{A}^{2} & \sigma_{AB} \\ \sigma_{AB} & \sigma_{B}^{2} \end{pmatrix} = \begin{pmatrix} 0.00016 & -0.000048 \\ -0.000048 & 0.00009 \end{pmatrix}$$

---

### 2. How to Calculate $\Sigma x$
The term $\Sigma x$ represents a matrix-vector multiplication. You multiply the variance-covariance matrix ($\Sigma$) by the allocation vector ($x$). The result is a new column vector where each row represents how much that specific asset's position covaries with the entire portfolio.

To calculate this, you multiply each row of the matrix by the column vector:

* **Row A Calculation:**
    $$(\Sigma x)_{A}=x_{A}\sigma_{A}^{2}+x_{B}\sigma_{AB}$$
    $$(\Sigma x)_{A}=(1,000,000 \times 0.00016) + (2,000,000 \times -0.000048)$$
    $$(\Sigma x)_{A}=160 - 96 = 64$$

* **Row B Calculation:**
    $$(\Sigma x)_{B}=x_{A}\sigma_{AB}+x_{B}\sigma_{B}^{2}$$
    $$(\Sigma x)_{B}=(1,000,000 \times -0.000048) + (2,000,000 \times 0.00009)$$
    $$(\Sigma x)_{B}=-48 + 180 = 132$$

So, your resulting vector for $\Sigma x$ is $\begin{pmatrix} 64 \\ 132 \end{pmatrix}$.

---

To understand how to calculate $\Sigma x$ and $x^\prime\Sigma x$, it helps to break down the linear algebra into simple, step-by-step arithmetic. In the context of portfolio risk, these calculations are used to find the total portfolio variance and the marginal risk contributions of individual assets.

Here is the step-by-step explanation based on the two-asset portfolio example provided in your document (Stock A and Stock B).

1. Define the Variables

First, identify your capital allocation vector ($x$) and your variance-covariance matrix ($\Sigma$).



$x$ (Capital Allocation Vector): This is a column matrix representing the dollar amount invested in each asset.

$$x = \begin{pmatrix} x_{A} \\ x_{B} \end{pmatrix} = \begin{pmatrix} 1,000,000 \\ 2,000,000 \end{pmatrix}$$





$\Sigma$ (Variance-Covariance Matrix): This matrix holds the daily variances ($\sigma^2$) on the diagonal and the covariance ($\sigma_{AB}$) on the off-diagonal.

$$\Sigma = \begin{pmatrix} \sigma_{A}^{2} & \sigma_{AB} \\ \sigma_{AB} & \sigma_{B}^{2} \end{pmatrix} = \begin{pmatrix} 0.00016 & -0.000048 \\ -0.000048 & 0.00009 \end{pmatrix}$$



2. How to Calculate $\Sigma x$

The term $\Sigma x$ represents a matrix-vector multiplication. You multiply the variance-covariance matrix ($\Sigma$) by the allocation vector ($x$). The result is a new column vector where each row represents how much that specific asset's position covaries with the entire portfolio.

To calculate this, you multiply each row of the matrix by the column vector:

Row A Calculation:



$$(\Sigma x)_{A}=x_{A}\sigma_{A}^{2}+x_{B}\sigma_{AB}$$



$$(\Sigma x)_{A}=(1,000,000 \times 0.00016) + (2,000,000 \times -0.000048)$$



$$(\Sigma x)_{A}=160 - 96 = 64$$



Row B Calculation:



$$(\Sigma x)_{B}=x_{A}\sigma_{AB}+x_{B}\sigma_{B}^{2}$$



$$(\Sigma x)_{B}=(1,000,000 \times -0.000048) + (2,000,000 \times 0.00009)$$



$$(\Sigma x)_{B}=-48 + 180 = 132$$



So, your resulting vector for $\Sigma x$ is $\begin{pmatrix} 64 \\ 132 \end{pmatrix}$.

3. How to Calculate $x^\prime\Sigma x$

The term $x^\prime\Sigma x$ calculates the total portfolio variance in dollar terms ($\sigma_{v}^{2}$).

The $x^\prime$ indicates the "transpose" of vector $x$, which simply turns the column vector into a row vector: $(x_{A}, x_{B})$. To find the final value, you take the dot product of this row vector $x^\prime$ and the column vector $\Sigma x$ you just calculated.

Using the $\Sigma x$ vector method:

$$x^\prime(\Sigma x) = x_{A}(\Sigma x)_{A} + x_{B}(\Sigma x)_{B}$$



$$x^\prime\Sigma x = (1,000,000 \times 64) + (2,000,000 \times 132)$$



$$x^\prime\Sigma x = 64,000,000 + 264,000,000 = 328,000,000$$

Using the expanded algebraic formula method:

Your document also shows calculating this all at once without explicitly finding the $\Sigma x$ vector first:



$$\sigma_{v}^{2}=x_{A}^{2}\sigma_{A}^{2}+x_{B}^{2}\sigma_{B}^{2}+2x_{A}x_{B}\sigma_{AB}$$



$$\sigma_{v}^{2}=(10^{6})^{2}(0.00016)+(2\times10^{6})^{2}(0.00009)+2(10^{6})(2\times10^{6})(-0.000048)$$



$$\sigma_{v}^{2}=160,000,000+360,000,000-192,000,000=328,000,000$$



Both methods arrive at the exact same portfolio variance.

Would you like me to walk through how these specific results (64, 132, and 328,000,000) plug directly into the Marginal VaR equation for Stock A and Stock B?


---

### 6. Backtesting VaR Models
Testing the accuracy of VaR models using historical exceptions.

* **Z-Test:** Tests if the number of exceptions ($N$) matches expectations.
    $$Z=\frac{N-pT}{\sqrt{p(1-p)T}}$$
    * **Example:** With 10 exceptions over 300 days at a 2% probability, $Z = \frac{10-6}{2.4249} \approx 1.65$. Since $1.65 < 1.96$, the model is not rejected at a 5% significance level.
* **Likelihood-Ratio Test for Unconditional Coverage ($LR_{uc}$):**
    $$LR_{uc}=-2\ln\left[\frac{(1-p)^{T-N}p^{N}}{(1-\hat{p})^{T-N}\hat{p}^{N}}\right]$$
    * **Example:** With $\hat{p} \approx 0.0333$, $LR_{uc} \approx 2.27$. Since $2.27 < 3.84$, the model's unconditional coverage is not rejected.
* **Likelihood-Ratio Test for Independence ($LR_{ind}$):** Tests if exceptions cluster together.
    $$LR_{ind}=-2\ln\left[\frac{(1-\hat{\pi})^{(T_{00}+T_{10})}\hat{\pi}^{(T_{01}+T_{11})}}{(1-\hat{\pi}_{0})^{T_{00}}\hat{\pi}_{0}^{T_{01}}(1-\hat{\pi}_{1})^{T_{10}}\hat{\pi}_{1}^{T_{11}}}\right]$$
    * **Example:** $LR_{ind} \approx 9.54$. Since $9.54 > 3.84$, the null hypothesis of independence is rejected, indicating unacceptable clustering of exceptions.
* **Likelihood-Ratio Test for Conditional Coverage ($LR_{cc}$):**
    $$LR_{cc}=LR_{uc}+LR_{ind}$$
    * **Example:** $0.7187 + 17.6214 = 18.3401$. The model is rejected at the 5% level because $18.3401 > 5.991$.

---

### 7. Regulatory Capital
* **Market Risk Charge (BCBS):**
    $$MRC_{t}^{IMA}=\max\left(k\cdot\frac{1}{60}\sum_{i=1}^{60}VaR_{t-i},VaR_{t-1}\right)+SRC_{t}$$
    * **Explanation:** The maximum is taken to represent both the historical average level of risk (over 60 periods) and the most current risk situation (the previous day). The VaR parameters used are a 99% significance level and a 10-day time horizon.

