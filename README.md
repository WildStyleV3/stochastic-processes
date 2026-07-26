# Stochastic Processes

Simulations of stochastic processes in Python.

This repository contains numerical experiments with:

1. Brownian Motion and Brownian Bridge
2. Geometric Brownian Motion (Euler-Maruyama vs. exact solution)
3. Stochastic Logistic Growth
4. Geometric Brownian Motion with time-varying, stress-dependent drift

The goal is to connect theoretical stochastic processes with applied simulations in statistics, finance, biology and engineering.

---

## 01. Brownian Motion and Brownian Bridge

The Brownian Motion is simulated using:

$$
W_i = W_{i-1} + \sqrt{\Delta t} Z_i
$$

where:

$$
Z_i \sim N(0,1)
$$

The Brownian Bridge is constructed as:

$$
BB_t = W_t - tW_1
$$

This forces the process to start and end at zero.

This is useful for understanding limit processes that appear in asymptotic statistics, such as stationarity tests and partial-sum processes.

---

## 02. Geometric Brownian Motion

The Geometric Brownian Motion is defined by the Itô stochastic differential equation:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

where:

- $S_t$ is the simulated state variable, interpreted here as a stock price.
- $\mu$ is the drift.
- $\sigma$ is the volatility.
- $W_t$ is a Brownian Motion.

The numerical approximation uses Euler-Maruyama:

$$
S_i = S_{i-1} + \mu S_{i-1}\Delta t + \sigma S_{i-1}\sqrt{\Delta t}Z_i
$$

This model can be interpreted as:

$$
\text{new state} = \text{previous state} + \text{deterministic trend} + \text{stochastic shock}
$$

## 03. Stochastic Logistic Growth

The deterministic logistic equation is:

$$
\frac{dX}{dt}=rX\left(1-\frac{X}{K}\right)
$$

The stochastic version adds multiplicative Brownian noise:

$$
dX_t=rX_t\left(1-\frac{X_t}{K}\right)dt+\sigma X_tdW_t
$$

When $\sigma=0$, the model reduces to the classical deterministic logistic growth curve.

When $\sigma>0$, the population fluctuates around the carrying capacity $K$, generating multiple possible trajectories.
---

## 04. Geometric Brownian Motion with time-varying drift

This extends the GBM idea from section 02 by making the drift $\mu_t$ a function of time, driven by a "stress" variable $S_t$ that switches to a higher level between $t=3$ and $t=7$:

$$
h(S_t) = 1 - e^{-\beta S_t}
$$

$$
\mu_t = \alpha \, h(S_t) - \gamma
$$

$$
dE_t = \mu_t E_t \, dt + \sigma_E E_t \, dW_t
$$

Because $\mu_t$ is deterministic given $S_t$, $\log E_t$ is still Gaussian with a time-dependent mean:

$$
M_t = \int_0^t \left(\mu_s - \tfrac{1}{2}\sigma_E^2\right) ds, \qquad \log E_t \sim N(M_t, \sigma_E^2 t)
$$

This is used to plot theoretical $\pm 2\sigma$ bands and the lognormal density of $E_T$ against the simulated paths, checking the Euler-Maruyama simulation against the closed-form distribution.

---

## Monte Carlo interpretation

Each simulated path is one possible future trajectory.

If we simulate many paths, we can estimate quantities such as:

$$
\mathbb{E}[S_T]
$$

$$
P(S_T < S_0)
$$

$$
P(S_T > K)
$$

and final price percentiles.

This does not predict the future directly. It generates possible outcomes under the assumptions of the model.

---

## Possible extensions

Future simulations may include:

- Ornstein-Uhlenbeck processes
- Mean-reverting models
- Stochastic volatility
- Jump diffusion models
- Synthetic time series for testing stationarity tests
- Kernel-based tests for non-stationarity

---

## Requirements

```bash
pip install numpy matplotlib
pip installl numpy
