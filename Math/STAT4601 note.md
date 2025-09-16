# Problem

## Mean and Variance Functions of a Time Series

$$Z_t = a_t - 0.5\, a_{t-1}, \quad \{a_t\}\ \text{i.i.d. with } \mathbb{E}[a_t]=0,\ \operatorname{Var}(a_t)=\sigma_a^2.$$

Step-by-step:

1) Mean function
- Use linearity of expectation:
$$\mathbb{E}[Z_t]=\mathbb{E}[a_t]-0.5\,\mathbb{E}[a_{t-1}] = 0 - 0.5\cdot 0 = 0.$$
- Hence the mean is constant (time-invariant):
$$\mu_Z(t)=0\ \text{for all } t.$$

2) Variance function
- Use variance of a linear combination and independence of a_t and a_{t-1}:
$$\operatorname{Var}(Z_t)=\operatorname{Var}(a_t - 0.5 a_{t-1})
= \operatorname{Var}(a_t) + 0.5^2 \operatorname{Var}(a_{t-1}) - 2\cdot 0.5\,\operatorname{Cov}(a_t,a_{t-1}).$$
- Since the a’s are i.i.d., $\operatorname{Var}(a_t)=\operatorname{Var}(a_{t-1})=\sigma_a^2$ and $\operatorname{Cov}(a_t,a_{t-1})=0$.
- Therefore:
$$\operatorname{Var}(Z_t) = \sigma_a^2 + 0.25\,\sigma_a^2 = 1.25\,\sigma_a^2 = \frac{5}{4}\,\sigma_a^2.$$

Answer:
- Mean function: $$\mu_Z(t)=0.$$
- Variance function: $$\operatorname{Var}(Z_t)=\frac{5}{4}\sigma_a^2\ \text{for all } t.$$


## Autocovariance and Autocorrelation Functions of a Time Series

Here, Zt is an MA(1): $$Z_t=a_t-0.5\,a_{t-1},\qquad \mathbb{E}[a_t]=0,\ \operatorname{Var}(a_t)=\sigma_a^2,\ \operatorname{Cov}(a_t,a_s)=0\ (t\neq s).$$

(c) Autocovariance function (ACVF) γ(h)
- Definition: $$\gamma(h)=\operatorname{Cov}(Z_{t+h},Z_t).$$

1) h=0
$$
\gamma(0)=\operatorname{Var}(Z_t)
=\operatorname{Var}(a_t-0.5a_{t-1})
=\sigma_a^2+0.25\sigma_a^2
=\tfrac{5}{4}\sigma_a^2.
$$

2) h=1
$$
\gamma(1)=\operatorname{Cov}(Z_{t+1},Z_t)
=\operatorname{Cov}(a_{t+1}-0.5a_t,\ a_t-0.5a_{t-1})
=-0.5\,\operatorname{Var}(a_t)
=-0.5\,\sigma_a^2.
$$

3) h=-1 (symmetry)
$$
\gamma(-1)=\gamma(1)=-0.5\,\sigma_a^2.
$$

4) |h|≥2
- The sets {a_{t+h}, a_{t+h-1}} and {a_t, a_{t-1}} share no common index, hence are independent:
$$
\gamma(h)=0,\quad |h|\ge 2.
$$

Summary:
$$
\gamma(h)=
\begin{cases}
\tfrac{5}{4}\sigma_a^2, & h=0,\\
-0.5\,\sigma_a^2, & h=\pm 1,\\
0, & |h|\ge 2.
\end{cases}
$$

(d) Autocorrelation function (ACF) ρ(h)
- Definition: $$\rho(h)=\dfrac{\gamma(h)}{\gamma(0)}.$$

Compute:
$$
\rho(0)=1,\qquad
\rho(\pm 1)=\frac{-0.5\,\sigma_a^2}{\tfrac{5}{4}\sigma_a^2}=-\frac{2}{5}=-0.4,\qquad
\rho(h)=0\ \text{for } |h|\ge 2.
$$

So the ACF cuts off after lag 1, as expected for an MA(1) with parameter θ=−0.5.


## Covariance Function of a Time Series

Because the noise terms {a_t} are i.i.d.

- “i.i.d.” means independent and identically distributed. Independence is the key part here.
- For any two different times s≠t, independence gives
  $$\mathbb{E}[a_t a_s]=\mathbb{E}[a_t]\mathbb{E}[a_s].$$
- Therefore the covariance is
  $$\operatorname{Cov}(a_t,a_{t-1})
  =\mathbb{E}[a_t a_{t-1}]-\mathbb{E}[a_t]\mathbb{E}[a_{t-1}]
  =\mathbb{E}[a_t]\mathbb{E}[a_{t-1}]-\mathbb{E}[a_t]\mathbb{E}[a_{t-1}]
  =0.$$

Since the problem states $\mathbb{E}[a_t]=0$, you can also see it directly as
$$\operatorname{Cov}(a_t,a_{t-1})=\mathbb{E}[a_t a_{t-1}]=\mathbb{E}[a_t]\mathbb{E}[a_{t-1}]=0.$$

Notes:
- Identical distribution is not needed for this step; independence alone implies zero covariance.
- Zero covariance does not generally imply independence, but i.i.d. does give independence, hence covariance zero for all nonzero lags.


## Stationarity of a Time Series

Stationarity in a time series means its statistical properties do not change over time. Intuitively, the process “looks the same” no matter when you observe it.

Common notions:
- Strict (strong) stationarity: The entire joint distribution of (X_t1, ..., X_tk) is invariant to shifts in time. This is the most stringent definition.
- Weak (covariance) stationarity: It’s enough that:
  - Mean is constant: E[X_t] = μ (doesn’t depend on t)
  - Variance is constant and finite: Var(X_t) = σ²
  - Autocovariance depends only on the lag h, not on t: Cov(X_t, X_{t+h}) = γ(h)

Implications:
- No deterministic trend or changing variance over time.
- No seasonality unless it’s been modeled/removed (raw seasonal patterns violate stationarity).

Why it matters:
- Many classical models (ARMA, SARIMA) and inference methods assume stationarity to ensure stable parameters and reliable forecasting.

Examples:
- Stationary: AR(1) with |φ| < 1.
- Non-stationary: Random walk X_t = X_{t-1} + ε_t (has a unit root), series with trends, seasonality, or structural breaks.

How to diagnose:
- Visual checks: mean/variance shifts, persistent ACF.
- Tests: ADF or Phillips–Perron (test for unit roots), KPSS (tests the null of stationarity). Often use ADF + KPSS together.

How to make a series stationary:
- Differencing (regular and/or seasonal).
- Detrending or de-seasonalizing.
- Variance-stabilizing transforms (log, Box–Cox, Yeo–Johnson).
- Modeling structural breaks or regime changes.

