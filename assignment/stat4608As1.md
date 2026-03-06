---
title: "STAT4608 Assignment 1"
author: "Zhu Yecheng 3036061373"
date: "2026-03-06"
geometry: margin=2cm
---

## Q1

$$R_1 (7/15) = -0.0303$$
$$R_2 (7/14) = -0.0116$$
$$R_3 (7/13) = 0.0239$$

**Simple Return:**
The $k$-period simple return is calculated as $R_t[k] = \prod_{j=0}^{k-1}(1+R_{t-j}) - 1$.


$$R_{3\text{-day}} = (1 - 0.0303)(1 - 0.0116)(1 + 0.0239) - 1$$

$$R_{3\text{-day}} = (0.9697)(0.9884)(1.0239) - 1 = 0.981358 - 1 = -0.018642 = -0.0186(3s.f.)$$
**Log Return:**
The $k$-period log return is calculated as $r_t[k] = \ln(1 + R_t[k])$.


$$r_{3\text{-day}} = \ln(0.981358) = -0.018818 = -0.0188(3s.f.)$$


## Q2

### (a) Non-parametric VaR at 98% confidence

$$Index = 252 \times 0.02 = 5.04$$


We use linear interpolation between the 5th and 6th ordered returns: $R_{(5)} = -2.5\%$ and $R_{(6)} = -2.4\%$



$$R^* = R_{(5)} \times 0.96 + R_{(6)} \times 0.04 = (-2.5) \times 0.96 + (-2.4) \times 0.04 = -2.496\%$$

Relative VaR: $$VaR(\mu) = V_0(\bar{R} - R^*)$$
$$VaR(\mu) = 100,000 \times (0.0004 - (-0.02496)) = 100,000 \times 0.02536 = \$2,536$$

Absolute VaR: $$VaR(0) = -V_0 R^*$$
$$VaR(0) = -100,000 \times (-0.02496) = \$2,496$$



### (b) Non-parametric Expected Shortfall at 98% confidence
Non-parametric ES is the sample mean of the observed losses that exceed the absolute VaR. There are exactly 5 returns worse than our cutoff of $-2.496\%$ ($R_{(1)}$ through $R_{(5)}$).
$$\text{Average of exceeding returns} = \frac{-7.2 - 5.3 - 3.0 - 2.6 - 2.5}{5} = -4.12\%$$
$$ES = 100,000 \times 0.0412 = \$4,120$$



### (c) Parametric normal VaR at 98% confidence
Assuming a normal distribution, we use the sample mean (0.04%) and standard deviation (0.5%). The Z-score for a 98% one-tailed confidence level ($1 - \alpha = 0.98$) is approximately $Z_{0.02} = 2.054$.

Relative VaR: $VaR(\mu) = V_0 Z_\alpha S$
$$VaR(\mu) = 100,000 \times 2.054 \times 0.005 = \$1,027$$

Absolute VaR: $VaR(0) = VaR(\mu) - V_0 \bar{R}$ 


$$VaR(0) = 1,027 - (100,000 \times 0.0004) = 1,027 - 40 = \$987$$



### (d) 10-day normal VaRs at 99% confidence
Under the Efficient Market Hypothesis (EMH), returns are i.i.d.. We scale the mean by 10 and the standard deviation by $\sqrt{10}$. We also use $Z_{0.01} = 2.326$.

$$\text{10-day Mean} = 10 \times 0.04\% = 0.4\%$$
$$\text{10-day Volatility} = \sqrt{10} \times 0.5\% \approx 1.5811\%$$

10-day Relative VaR:
$$VaR_{99\%}(\mu)[10] = 100,000 \times 2.326 \times 0.015811 = \$3,677.64$$

10-day Absolute VaR:
$$VaR_{99\%}(0)[10] = 3,677.64 - (100,000 \times 0.004) = \$3,277.64$$





## Q3

Given $T = 300$, exceptions $N = 10$, and required probability $p = 0.02$.

### (a) Z Test (5% significance level)


$$Z = \frac{N - pT}{\sqrt{p(1-p)T}}$$

- Expected exceptions $pT = 300 \times 0.02 = 6$
- Standard error = $\sqrt{0.02 \times 0.98 \times 300} = \sqrt{5.88} \approx 2.4249$
- $Z = \frac{10 - 6}{2.4249} \approx 1.65$

Conclusion: Since $1.65 < 1.96$ (the critical value for a two-sided test at 5%), we do not reject the VaR model.



### (b) Likelihood-Ratio Test for Unconditional Coverage ($LR_{uc}$)
Here, observed probability $\hat{p} = \frac{10}{300} \approx 0.0333$.

$$LR_{uc} = -2 \ln \left[ \frac{(1-p)^{T-N} p^N}{(1-\hat{p})^{T-N} \hat{p}^N} \right]$$

$$LR_{uc} = -2 \ln \left[ \frac{(0.98)^{290} (0.02)^{10}}{(0.9667)^{290} (0.0333)^{10}} \right] \approx 2.27$$

Conclusion: The critical value for $\chi^2(1)$ at 5% is 3.84. Since $2.27 < 3.84$, we do not reject the model's unconditional coverage.



### (c) Likelihood-Ratio Test for Independence ($LR_{ind}$)
Using the Markov state parameters:

- $T_{11} = 3$ (exceptions following an exception)
- $T_1 = 10$ (total exceptions). Thus, $T_{01} = T_1 - T_{11} = 7$
- Assuming $T_{01} = T_{10}$, $T_{10} = 7$
- $T_0 = 290$ (non-exceptions). Thus, $T_{00} = T_0 - T_{10} = 283$
- Probabilities: $\hat{\pi}_0 = \frac{7}{290} \approx 0.0241$, $\hat{\pi}_1 = \frac{3}{10} = 0.30$, and $\hat{\pi} = \frac{10}{300} \approx 0.0333$



$$LR_{ind} = -2 \ln \left[ \frac{(1-\hat{\pi})^{(T_{00}+T_{10})} \hat{\pi}^{(T_{01}+T_{11})}}{(1-\hat{\pi}_0)^{T_{00}} \hat{\pi}_0^{T_{01}} (1-\hat{\pi}_1)^{T_{10}} \hat{\pi}_1^{T_{11}}} \right]$$



$$LR_{ind} = -2 \ln \left[ \frac{(0.9667)^{290}(0.0333)^{10}}{(0.9759)^{283}(0.0241)^7(0.70)^7(0.30)^3} \right] \approx 9.54$$

Conclusion: Since $9.54 > 3.84$, we reject the null hypothesis of independence at the 5% level of significance. The exceptions are clustering unacceptably.



## Q4

First, convert the annual parameters to daily parameters assuming 250 trading days:
- $\sigma_A^2 = \frac{0.20^2}{250} = 0.00016$
- $\sigma_B^2 = \frac{0.15^2}{250} = 0.00009$
- Covariance $\sigma_{AB} = \frac{-0.4 \times 0.20 \times 0.15}{250} = -0.000048$

### (a) Daily diversified portfolio VaR at 99%
Let the capital allocations be $x_A = 1{,}000{,}000$ and $x_B = 2{,}000{,}000$. The portfolio variance in dollar terms is $\sigma_v^2 = x^{\prime}\Sigma x$.


$$\sigma_v^2 = x_A^2 \sigma_A^2 + x_B^2 \sigma_B^2 + 2x_A x_B \sigma_{AB}$$

$$\sigma_v^2 = (10^6)^2(0.00016) + (2 \times 10^6)^2(0.00009) + 2(10^6)(2 \times 10^6)(-0.000048)$$

$$\sigma_v^2 = 160,000,000 + 360,000,000 - 192,000,000 = 328,000,000$$


Volatility $\sigma_v = \sqrt{328,000,000} \approx 18,110.77$.
Using $Z_{0.01} = 2.326$, the relative Diversified Portfolio VaR is:


$$VaR_p = 2.326 \times 18,110.77 = \$42,125.65$$

### (b) Daily undiversified VaRs at 99%
This is the simple sum of the individual VaRs:
$$VaR_A = 2.326 \times \sqrt{160,000,000} = \$29,421.83$$

$$VaR_B = 2.326 \times \sqrt{360,000,000} = \$44,132.75$$

Undiversified VaR: $$29,421.83 + 44,132.75 = \$73,554.58$$ 


### (c) Daily marginal VaRs at 99%
Marginal VaR measures the risk contribution per unit of capital. $\Delta VaR = VaR_p \frac{\Sigma x}{x^{\prime}\Sigma x}$.

First, calculate the vector $\Sigma x$:
Row A: $$(\Sigma x)_A = x_A \sigma_A^2 + x_B \sigma_{AB} = 160 - 96 = 64$$

Row B: $$(\Sigma x)_B = x_A \sigma_{AB} + x_B \sigma_B^2 = -48 + 180 = 132$$

Using $\sigma_v^2 = 328,000,000$ (which is $x^{\prime}\Sigma x$):
$$\Delta VaR_A = 42,125.65 \times \frac{64}{328,000,000} \approx 0.008220$$
$$\Delta VaR_B = 42,125.65 \times \frac{132}{328,000,000} \approx 0.016953$$

### (d) Daily component VaRs at 99%

$$CVaR_A = 0.008220 \times 1,000,000 = \$8,220$$
$$CVaR_B = 0.016953 \times 2,000,000 = \$33,906$$