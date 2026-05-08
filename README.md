# Stochastic Processes

Simulations of stochastic processes in Python.

This repository contains numerical experiments with:

1. Brownian Motion
2. Brownian Bridge
3. Geometric Brownian Motion
4. Monte Carlo simulation of stochastic differential equations

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

- Stochastic logistic growth
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
