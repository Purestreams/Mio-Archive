# SDST4608/STAT4608 Market Risk Analysis Assignment 2

(Due on April 19, 2026)

---

**1.** Consider a portfolio of two assets with daily **mean corrected simple returns** $\{r_{i,t}\}_{t=1}^{252}$, $i=1, 2$, respectively. It is estimated by the EWMA method with $\lambda=0.9$ that

$$\hat{\sigma}_{1,252}^{2} = \widehat{\text{Var}}(r_{1,252}) = 0.001,$$
$$\hat{\sigma}_{2,252}^{2} = \widehat{\text{Var}}(r_{2,252}) = 0.004,$$
$$\widehat{\text{Cov}}_{252} = \widehat{\text{Cov}}(r_{1,252}, r_{2,252}) = -0.001.$$

Given that $r_{1,252} = 0.02$ and $r_{2,252} = 0.05$, and the weights of two assets are $w_{1,252} = 0.4$ and $w_{2,252} = 0.6$, respectively.

- **(a)** Find the EWMA estimates $\hat{\sigma}_{1,253}^{2}$, $\hat{\sigma}_{2,253}^{2}$ and $\widehat{\text{Cov}}_{253}$, respectively. **[6 marks]**
- **(b)** Find the diversified VaR of the portfolio at the 95% confidence level, in percentage, at time $t=253$, based on your results in part (a). **[6 marks]**
- **(c)** Find the marginal VaRs of the portfolio at time $t=253$. **[4 marks]**

**[Total: 16 marks]**

---

**2.** Consider a sequence of daily simple returns of an asset, $\{R_{t} : 1 \le t \le 400\}$, with the latest three observations given by

$$R_{400} = 0.02, \quad R_{399} = -0.01, \quad R_{398} = 0.01.$$

The following AR(2)-GARCH(1,1) model was fitted to the returns.

$$
\begin{cases}
R_{t} = 0.004 + 0.5R_{t-1} - 0.3R_{t-2} + a_{t}, \\
a_{t} = \sigma_{t}\epsilon_{t}, \qquad \{\epsilon_{t}\} \stackrel{\text{iid}}{\sim} N(0,1), \\
\sigma_{t}^{2} = 0.0005 + 0.35a_{t-1}^{2} + 0.55\sigma_{t-1}^{2},
\end{cases}
$$

with the latest fitted value $\sigma_{400}^{2} = 0.0025$. Find the following percentage VaRs (assuming initial capital $V_{0} = \$1$).

- **(a)** Find the 95% daily relative VaR and absolute VaR of the investment at time $t=401$. **[8 marks]**
- **(b)** Find the 95% daily relative VaR and absolute VaR of the investment at time $t=402$. **[8 marks]**
- **(c)** Find the 95% two-days relative VaR and absolute VaR of the investment for the period from $t=400$ to 402. **[8 marks]**

**[Total: 24 marks]**

---

**3.** A portfolio value $V$ is mapped as a function of a single risk factor value $S$ in the following form, $V(S) = S^{3} - 30S^{2} + 300S + 150$. Given that the risk factor has a current value $S_{0} = \$8$, and its return follows a normal distribution with an annual volatility $\sigma=0.3$.

- **(a)** Approximate the 95% portfolio VaR by the Delta-Normal method. **[2 marks]**
- **(b)** Approximate the 95% portfolio VaR by the Delta-Gamma method. **[2 marks]**
- **(c)** Approximate the 95% portfolio VaR by the Delta-Gamma-Delta method. **[2 marks]**
- **(d)** Which of the above approximation methods do you prefer? Briefly explain. **[2 marks]**
- **(e)** If the current value is $S_{0} = \$10$, will the above approximation methods work well? Briefly explain. **[2 marks]**

**[Total: 10 marks]**