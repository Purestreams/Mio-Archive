
# A practical guide to identifying suitable ARIMA models (with sample lag tables)

This guide shows a step‑by‑step workflow to choose ARIMA models using plots, ACF/PACF “fingerprints,” simple tests, and diagnostics. It includes small sample lag tables you can mimic when analyzing your own series.

ARIMA means ARIMA(p,d,q), where:
- $d$ = order of nonseasonal differencing (to remove stochastic trends)
- $p$ = AR order (lags of $Z_t$)
- $q$ = MA order (lags of shocks $a_t$)

Seasonal (SARIMA) extends to ARIMA$(p,d,q)\times(P,D,Q)_s$ with seasonal period $s$.

Throughout, let $\nabla=(1-B)$ be the difference operator, $B$ the backshift ($BZ_t=Z_{t-1}$), and $\{a_t\}$ white noise with variance $\sigma_a^2$.

## Step 0. Plot and stabilize variance if needed
- Plot $Z_t$ and its histogram.
- If variance changes with level, consider a Box–Cox transform $Y_t=\mathrm{BC}_\lambda(Z_t)$:
  $$
  Y_t=\begin{cases}
  \dfrac{Z_t^\lambda-1}{\lambda}, & \lambda\ne 0,\\[4pt]
  \ln Z_t, & \lambda=0.
  \end{cases}
  $$
Apply the following steps to $Y_t$ if you transform.

## Step 1. Decide $d$ (how many differences)
Clues and tests:
- Slow, very high, smooth decay in ACF of $Z_t$ suggests a unit root → try $d=1$.
- After differencing once, if ACF at lag 1 is strongly negative (e.g., $\rho_1\lesssim-0.5$), you may have overdifferenced; consider reducing $d$.
- Use unit‑root/stationarity tests jointly:
  - Augmented Dickey–Fuller (ADF): fail to reject → difference more.
  - KPSS: reject stationarity → difference more.
Choose the smallest $d$ that removes the stochastic trend.

Seasonal: if large spikes at lags $s,2s,\dots$ that decay slowly, try seasonal differencing $D=1$ using $(1-B^s)$.

## Step 2. Use ACF/PACF shapes to choose $(p,q)$
Once the series is made stationary (after differencing $d$ and seasonal differencing $D$ if any), inspect the ACF and PACF of the stationary series (not the original).

Rules of thumb:
- AR(p): PACF “cuts off” at lag $p$, ACF tails off (often roughly geometric/damped sine).
- MA(q): ACF “cuts off” at lag $q$, PACF tails off.
- ARMA(p,q): both ACF and PACF tail off (no sharp cutoffs).
- Alternating signs with geometric decay often indicates a negative AR parameter; strong one‑step negative ACF with quick taper suggests MA(1).

Approximate 95% bounds for white‑noise ACF at lag $k$:
$$
\pm \frac{1.96}{\sqrt{n}}.
$$

## Step 3. Estimate and compare plausible models
Fit several candidates that match the patterns. Rank with information criteria:
- AIC: $\mathrm{AIC} = -2\ell + 2k$
- AICc (recommended for small $n$): $\mathrm{AICc} = \mathrm{AIC} + \dfrac{2k(k+1)}{n-k-1}$
- BIC: $\mathrm{BIC} = -2\ell + k\ln n$
Here $\ell$ is the maximized log‑likelihood and $k$ the number of estimated parameters (include variance, constants, and seasonal terms).

Prefer lower AICc/BIC, but don’t ignore diagnostics.

## Step 4. Diagnostic checking
On the fitted model’s residuals $\hat a_t$:
- Residual ACF: all lags within $\pm 1.96/\sqrt{n}$ without structure.
- Portmanteau test (Ljung–Box) for $m$ lags:
  $$
  Q(m)=n(n+2)\sum_{k=1}^m\frac{\hat\rho_k^2}{n-k}
  $$
  A large p‑value suggests residuals are white noise.
- Check normality (QQ plot) and constant variance.
- Ensure stationarity/invertibility: roots of AR and MA polynomials must lie outside the unit circle.

If diagnostics fail, revisit orders or differencing.

---

## Sample lag tables (ACF/PACF “fingerprints”)

Below are stylized lag tables (rounded) that you can use as references. Values beyond the first few lags should typically taper toward 0.

1) Stationary AR(1) with $\phi=0.6$ (no differencing)

| Lag k | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| ACF | 0.60 | 0.36 | 0.22 | 0.13 | 0.08 | 0.05 |
| PACF | 0.60 | ~0 | ~0 | ~0 | ~0 | ~0 |

Interpretation: PACF cuts off at lag 1; ACF decays geometrically → ARIMA(1,0,0).

2) Stationary MA(1) with $\theta=0.7$ (no differencing)

ACF for MA(1): $\rho(1)=\dfrac{\theta}{1+\theta^2}\approx 0.7/1.49\approx 0.47$; $\rho(k)=0$ for $k\ge 2$.

| Lag k | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| ACF | 0.47 | ~0 | ~0 | ~0 | ~0 | ~0 |
| PACF | 0.47 | 0.22 | 0.10 | 0.05 | 0.02 | 0.01 |

Interpretation: ACF cuts off at lag 1; PACF tails off → ARIMA(0,0,1).

3) Integrated series needing one difference; differenced series is MA(1)

Suppose $(1-B)Z_t = a_t - 0.6 a_{t-1}$.

| Lag k | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| ACF of $Z_t$ | 0.98 | 0.96 | 0.94 | 0.92 | 0.90 | 0.88 |
| ACF of $\nabla Z_t$ | −0.47 | ~0 | ~0 | ~0 | ~0 | ~0 |

Interpretation: Original series has near‑unit‑root ACF; differenced series shows MA(1) → ARIMA(0,1,1).

4) Integrated series; differenced series looks ARMA(1,1) with alternation

Example ACFs similar to the prompt in many textbooks:

| Lag k | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| ACF of $Z_t$ | 0.97 | 0.94 | 0.90 | 0.86 | 0.81 | 0.76 | 0.71 |
| ACF of $\nabla Z_t$ | −0.53 | 0.41 | −0.35 | 0.21 | −0.16 | 0.15 | 0.08 |

Interpretation: One difference needed; differenced ACF alternates with damping → ARMA(1,1) on differences → ARIMA(1,1,1).

5) Seasonal signal with $s=12$ and seasonal difference $D=1$

| Lag k | 1 | 2 | … | 11 | 12 | 13 | 24 |
|---|---:|---:|---:|---:|---:|---:|---:|
| ACF | small | small | … | small | big spike | small | spike |
| PACF | may show spike at 12 if SAR present |

Interpretation: Spikes at multiples of 12 suggest seasonal AR or MA terms; start with SARIMA $(p,d,q)\times(P,1,Q)_{12}$.

---

## Sample filled lag table (illustrative)

Suppose $n=100$ (so bounds ≈ ±0.196). The following values are typical of a series that likely needs one difference and then shows low-order ARMA behavior:

| Lag | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Sample ACF of $Z_t$ | 0.96 | 0.95 | 0.94 | 0.92 | 0.88 | 0.87 | 0.86 | 0.84 |
| Sample PACF of $Z_t$ | 0.96 | 0.40 | 0.12 | -0.07 | -0.02 | -0.13 | 0.08 | -0.11 |
| Sample ACF of $\nabla Z_t$ | -0.46 | 0.09 | 0.09 | -0.04 | -0.08 | 0.09 | -0.06 | -0.02 |
| Sample PACF of $\nabla Z_t$ | -0.46 | -0.08 | 0.23 | -0.03 | 0.13 | -0.11 | -0.01 | -0.09 |

Interpretation at a glance:
- $Z_t$ ACF very high and decaying slowly → likely nonstationary (unit root).
- After differencing, the ACF values are small (many within bounds) with a notable negative spike at lag 1 → suggests an MA(1) component in the differenced data.


### Fingerprints: how ACF/PACF imply $(p,d,q)$

Decide $d$ first, then choose $(p,q)$ on the stationary series (after differencing).

### 3.1 Decide the differencing order $d$

Heuristics:
- If ACF of $Z_t$ stays very high and decays slowly (no clear cutoff): try $d=1$.
- If after one difference, $\rho_{\nabla Z}(1)$ is strongly negative (≈ −0.4 to −0.6) and the rest near 0, you likely used the correct $d$ (common with ARIMA$(0,1,1)$). If many large lags remain, the differenced series still has AR terms (consider ARIMA$(p,1,q)$ with $p>0$).
- Formal tests to confirm:
  - ADF test (look for rejection of unit root after differencing).
  - KPSS test (stationarity not rejected after differencing).

Keep $d$ as small as possible (avoid overdifferencing).

### 3.2 Identify $(p,q)$ on the stationary series

Rules of thumb (nonseasonal):
- AR($p$): PACF “cuts off” at $p$, ACF tails off (geometric/damped sine).
- MA($q$): ACF “cuts off” at $q$, PACF tails off.
- ARMA($p,q$): both ACF and PACF tail off (no sharp cutoffs).
- Alternating signs with geometric damping suggests a negative AR parameter.

Seasonal: spikes at multiples of $s$ → add seasonal terms $(P,D,Q)_s$.


---

## Quick decision chart (nonseasonal)

1) Is $Z_t$ stationary?
- If ACF decays very slowly and ADF fails to reject: set $d\leftarrow d+1$ and analyze $\nabla Z_t$.
- If after differencing, $\rho_1$ is strongly negative (≈ −0.5 or lower), consider you may have overdifferenced.

2) For the (seasonally) differenced series:
- PACF cuts off at lag $p$ and ACF tails → add AR terms → increase $p$.
- ACF cuts off at lag $q$ and PACF tails → add MA terms → increase $q$.
- Both tail → consider ARMA($p,q$) with small orders.

3) Fit candidates and choose via AICc/BIC, then validate with residual diagnostics.

---

## Useful formulas and heuristics

- Sample ACF:
  $$
  \hat\rho_k=\frac{\sum_{t=k+1}^{n}(Z_t-\bar Z)(Z_{t-k}-\bar Z)}{\sum_{t=1}^n(Z_t-\bar Z)^2}.
  $$
- AR(1) theoretical ACF: $\rho_k=\phi^k$.
- MA(1) theoretical ACF: $\rho_1=\dfrac{\theta}{1+\theta^2}$, $\rho_k=0$ for $k\ge 2$.
- ARMA(1,1), rough identification on a stationary series:
  - Ratio $\rho_{k+1}/\rho_k\approx \phi$ for $k\ge 2$.
  - Lag‑1 ACF:
    $$
    \rho_1=\frac{(\phi+\theta)(1+\phi\theta)}{1+2\phi\theta+\theta^2}.
    $$
- Approximate white‑noise bounds for ACF: $\pm 1.96/\sqrt{n}$.

---

## Worked micro‑example: concluding ARIMA(1,1,1)
Suppose your lag table matches example (4). The original ACF is near a unit root; after one difference the ACF alternates with damping.

- Choose $d=1$.
- From $\nabla Z_t$ ACF, estimate $\phi \approx \rho_2/\rho_1 \approx 0.41/(-0.53)\approx -0.77$ (rule of thumb for ARMA(1,1)).
- Use the ARMA(1,1) lag‑1 formula to get a starting $\theta$ (solve numerically), often around $\theta\approx 0.3$–$0.4$ here.
- Fit ARIMA(1,1,1), compare against ARIMA(0,1,1) and ARIMA(1,1,0) via AICc; keep the one that passes residual diagnostics.

---

## Seasonal checklist (SARIMA)
- If seasonality with period $s$ is present, try $D=1$ first: analyze $(1-B^s)\nabla^d Z_t$.
- Seasonal ACF spikes at $s,2s,\dots$ suggest seasonal MA($Q$); PACF spikes at $s,2s,\dots$ suggest seasonal AR($P$).
- Keep $(P,Q)$ small (0–2). Fit SARIMA$(p,d,q)\times(P,D,Q)_s$, compare via AICc, and run residual diagnostics.

---

## Minimal code to reproduce lag tables (optional)

Python (statsmodels):
```python
import numpy as np
import statsmodels.api as sm

# x is your series (numpy array)
acf_vals = sm.tsa.stattools.acf(x, nlags=20, fft=True)
pacf_vals = sm.tsa.stattools.pacf(x, nlags=20, method="ywm")
```

R (forecast/fable):
```r
acf(x, lag.max = 20, plot = TRUE)
pacf(x, lag.max = 20, plot = TRUE)
# Automated but validate!:
forecast::auto.arima(x, seasonal = TRUE)
```

---

## Final checklist
- Transform (if needed), difference minimally ($d$ and possibly $D$).
- Read ACF/PACF “fingerprints” to pick small $(p,q)$ (and $(P,Q)$).
- Fit several candidates; compare AICc/BIC.
- Validate with residual ACF and Ljung–Box.
- Ensure stationarity/invertibility and interpretability.
- Iterate until residuals are white noise and model is parsimonious.

If you share your own lag table (ACF/PACF), I can walk you to a concrete ARIMA specification and starting parameter values.