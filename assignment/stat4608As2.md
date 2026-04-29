---
title: "STAT4608 Assignment 2"
author: "Zhu Yecheng 3036061373"
date: "2026-04-19"
geometry: margin=2cm
---

## Q1

Given $\lambda=0.9$, and EWMA updates

$$\hat{\sigma}_{i,t+1}^2 = \lambda\hat{\sigma}_{i,t}^2 + (1-\lambda)r_{i,t}^2,$$
$$\widehat{\text{Cov}}_{t+1} = \lambda\widehat{\text{Cov}}_t + (1-\lambda)r_{1,t}r_{2,t}.$$

### (a) EWMA estimates at $t=253$

$$\hat{\sigma}_{1,253}^2 = 0.9(0.001)+0.1(0.02^2)=0.00094$$

$$\hat{\sigma}_{2,253}^2 = 0.9(0.004)+0.1(0.05^2)=0.00385$$

$$\widehat{\text{Cov}}_{253} = 0.9(-0.001)+0.1(0.02\times0.05)=-0.0008$$

### (b) 95% diversified portfolio VaR at $t=253$ (in %)

Portfolio variance:

$$\hat{\sigma}_{p,253}^2 = w_1^2\hat{\sigma}_{1,253}^2+w_2^2\hat{\sigma}_{2,253}^2+2w_1w_2\widehat{\text{Cov}}_{253}$$

$$\hat{\sigma}_{p,253}^2 = 0.4^2(0.00094)+0.6^2(0.00385)+2(0.4)(0.6)(-0.0008)=0.00115$$

$$\hat{\sigma}_{p,253}=\sqrt{0.00115}=0.0339$$

Using $z_{0.05}=1.645$,

$$\text{Diversified VaR}_{95\%}=1.645\times0.0339=0.0558\approx 5.58\%$$

### (c) Marginal VaRs at $t=253$

For $\Sigma=\begin{pmatrix}0.00094 & -0.0008\\ -0.0008 & 0.00385\end{pmatrix}$ and $w=(0.4,0.6)'$,

$$\Sigma w=\begin{pmatrix}0.00094(0.4)-0.0008(0.6)\\ -0.0008(0.4)+0.00385(0.6)\end{pmatrix}=\begin{pmatrix}-0.000104\\0.00199\end{pmatrix}.$$

Marginal VaR formula:

$$\text{MVaR}_i=z_{0.05}\frac{(\Sigma w)_i}{\sigma_p}.$$

So

$$\text{MVaR}_1=1.645\frac{-0.000104}{0.0339}=-0.00504\approx-0.504\%,$$
$$\text{MVaR}_2=1.645\frac{0.00199}{0.0339}=0.0964\approx9.64\%.$$


## Q2

Model:

$$R_t=0.004+0.5R_{t-1}-0.3R_{t-2}+a_t,$$
$$a_t=\sigma_t\epsilon_t,\quad \epsilon_t\sim N(0,1),$$
$$\sigma_t^2=0.0005+0.35a_{t-1}^2+0.55\sigma_{t-1}^2,$$
with $R_{400}=0.02$, $R_{399}=-0.01$, $R_{398}=0.01$, $\sigma_{400}^2=0.0025$.

We use $z_{0.05}=1.645$, $V_0=1$,

$$\text{Relative VaR}_{95\%}=z_{0.05}\sigma,\qquad \text{Absolute VaR}_{95\%}=z_{0.05}\sigma-\mu.$$

First, recover $a_{400}$:

$$a_{400}=R_{400}-\left(0.004+0.5R_{399}-0.3R_{398}\right)$$
$$=0.02-\left(0.004+0.5(-0.01)-0.3(0.01)\right)=0.0240.$$

### (a) 95% daily VaRs at $t=401$

Conditional mean:

$$\mu_{401|400}=0.004+0.5(0.02)-0.3(-0.01)=0.0170.$$

Conditional variance:

$$\sigma_{401|400}^2=0.0005+0.35(0.024)^2+0.55(0.0025)=0.00208,$$
$$\sigma_{401|400}=\sqrt{0.00208}=0.0456.$$



$$\text{VaR}_{401}^{\text{rel}}=1.645(0.0456)=0.0750\approx7.50\%.$$



$$\text{VaR}_{401}^{\text{abs}}=0.0750-0.0170=0.0580\approx5.80\%.$$

### (b) 95% daily VaRs at $t=402$

Two-step conditional mean:

$$\mu_{402|400}=0.004+0.5\mu_{401|400}-0.3R_{400}$$
$$=0.004+0.5(0.017)-0.3(0.02)=0.00650.$$

For GARCH forecast, $E(a_{401}^2|\mathcal F_{400})=\sigma_{401|400}^2$, so

$$\sigma_{402|400}^2=0.0005+(0.35+0.55)\sigma_{401|400}^2$$
$$=0.0005+0.9(0.00208)=0.00237,$$
$$\sigma_{402|400}=\sqrt{0.00237}=0.0487.$$



$$\text{VaR}_{402}^{\text{rel}}=1.645(0.0487)=0.0801\approx8.01\%.$$



$$\text{VaR}_{402}^{\text{abs}}=0.0801-0.00650=0.0736\approx7.36\%.$$

### (c) 95% two-days VaRs for period $400\to402$

Let $R_{[401,402]}=R_{401}+R_{402}$.

Mean:

$$\mu_{[401,402]|400}=\mu_{401|400}+\mu_{402|400}=0.0170+0.00650=0.0235.$$

Because

$$R_{401}=\mu_{401|400}+a_{401},$$
$$R_{402}=\mu_{402|400}+0.5a_{401}+a_{402},$$

we have

$$\text{Cov}(R_{401},R_{402}|\mathcal F_{400})=0.5\sigma_{401|400}^2=0.00104.$$

Also,

$$\text{Var}(R_{401}|\mathcal F_{400})=\sigma_{401|400}^2=0.00208,$$
$$\text{Var}(R_{402}|\mathcal F_{400})=0.25\sigma_{401|400}^2+\sigma_{402|400}^2=0.00289.$$

Hence

$$\sigma_{[401,402]|400}^2=\text{Var}(R_{401})+\text{Var}(R_{402})+2\text{Cov}(R_{401},R_{402})$$
$$=0.00208+0.00289+2(0.00104)=0.00704,$$
$$\sigma_{[401,402]|400}=\sqrt{0.00704}=0.0839.$$



$$\text{VaR}_{[401,402]}^{\text{rel}}=1.645(0.0839)=0.138\approx13.8\%.$$



$$\text{VaR}_{[401,402]}^{\text{abs}}=0.138-0.0235=0.115\approx11.5\%.$$

## Q3

Given

$$V(S)=S^3-30S^2+300S+150,\qquad S_0=8,\qquad \sigma_R=0.3.$$

Assume one-period factor return $R\sim N(0,0.3^2)$, so

$$\Delta S\approx S_0R,\qquad \sigma_{\Delta S}=S_0\sigma_R=8(0.3)=2.40.$$

At $S_0=8$:

$$\Delta=V'(S_0)=3S_0^2-60S_0+300=12.0,$$
$$\Gamma=V''(S_0)=6S_0-60=-12.0,$$
$$D=V'''(S_0)=6.00.$$

Take $q_{0.05}(\Delta S)=z_{0.05}\sigma_{\Delta S}=-1.645(2.40)=-3.948\approx-3.95$.

### (a) Delta-Normal VaR (95%)

$$\Delta V\approx \Delta\,\Delta S,\qquad \text{VaR}\approx1.645|\Delta|\sigma_{\Delta S}$$

$$\text{VaR}_{DN}=1.645(12.0)(2.40)=47.4.$$

### (b) Delta-Gamma VaR (95%)

$$\Delta V\approx \Delta\Delta S+\frac12\Gamma(\Delta S)^2.$$

At $\Delta S=-3.95$:

$$\Delta V\approx12.0(-3.95)+\frac12(-12.0)(-3.95)^2=-141,$$

so

$$\text{VaR}_{DG}\approx141.$$

### (c) Delta-Gamma-Delta VaR (95%)

Include the third-order term:

$$\Delta V\approx\Delta\Delta S+\frac12\Gamma(\Delta S)^2+\frac16D(\Delta S)^3.$$

At $\Delta S=-3.948$ (using the unrounded shock in the nonlinear term):

$$\Delta V\approx12.0(-3.948)+\frac12(-12.0)(-3.948)^2+\frac16(6.00)(-3.948)^3=-202.433,$$

hence

$$\text{VaR}_{DGD}\approx202.$$

### (d) Preferred method

I prefer **Delta-Gamma-Delta** here, because $V(S)$ is exactly a cubic function, so the third-order Taylor expansion captures the mapping much better than first- or second-order approximations.

### (e) 

At $S_0=10$,

$$V'(10)=0.00,\qquad V''(10)=0.00,\qquad V'''(10)=6.00.$$

So Delta-Normal and Delta-Gamma both collapse (near-zero VaR), which means it is poor. 

The third-order method remains informative. Therefore, the first two methods do **not** work well at $S_0=10$.