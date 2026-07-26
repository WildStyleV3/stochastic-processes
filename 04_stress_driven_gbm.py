import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

m, n, T = 200, 1000, 10
dt = T/(n-1)
t = np.linspace(0, T, n)
Zt = np.random.normal(0, 1, (n, m))

alpha, beta, gamma, sigma_E = 0.3, 1.0, 0.05, 0.1
S_t = np.where((t >= 3) & (t <= 7), 0.8, 0.1)
h_S = 1 - np.exp(-beta * S_t)
mu_t = alpha * h_S - gamma

E = np.zeros((n, m)); E[0] = 1
for i in range(1, n):
    E[i] = E[i-1] + mu_t[i]*E[i-1]*dt + sigma_E*E[i-1]*np.sqrt(dt)*Zt[i]

# --- teoría: log E_t ~ N(M_t, sigma^2 t) ---
M_t = np.cumsum(mu_t - sigma_E**2/2) * dt
M_t = M_t - M_t[0]                    # anclar en 0 para t=0
sd_t = sigma_E * np.sqrt(t)
banda_sup = np.exp(M_t + 2*sd_t)
banda_inf = np.exp(M_t - 2*sd_t)























# --- figura ---
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(11, 6), sharey=True,
    gridspec_kw={'width_ratios': [3, 1], 'wspace': 0.05}
)

ax1.plot(t, E, lw=0.6, alpha=0.6)
ax1.plot(t, banda_sup, 'k--', lw=1.2)
ax1.plot(t, banda_inf, 'k--', lw=1.2)
ax1.plot(t, np.exp(M_t), 'k-', lw=1.5)      # mediana teórica
ax1.set_xlabel("Time t"); ax1.set_ylabel("$E_t$")
ax1.set_title("Geometric Brownian Motion sample paths")

# densidad lognormal teórica de E_T, dibujada de lado
y = np.linspace(E[-1].min()*0.7, E[-1].max()*1.3, 400)
dens = lognorm.pdf(y, s=sd_t[-1], scale=np.exp(M_t[-1]))
ax2.plot(dens, y, 'k-', lw=1.2)
ax2.plot(np.zeros(m), E[-1], '|', color='k', ms=6, alpha=0.4)  # rug
ax2.axhline(np.exp(M_t[-1]), color='k', lw=0.8)
ax2.set_xlabel("Lognormal density")
ax2.set_title("Final value $E_T$")

plt.show()