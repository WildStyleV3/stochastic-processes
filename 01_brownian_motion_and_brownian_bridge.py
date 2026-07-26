import numpy as np
import matplotlib.pyplot as plt

n_paths = 1000
n_steps = 1000
brownian_paths = np.zeros((n_steps, n_paths))
Z = np.random.normal(0, 1, (n_steps, n_paths))
dt = 1 / (n_steps - 1)
sigma = 1
# Brownian Motion
for i in range(1, n_steps):
    brownian_paths[i] = brownian_paths[i - 1] + sigma * np.sqrt(dt) * Z[i]
# Brownian Bridge
t = np.linspace(0, 1, n_steps).reshape(n_steps, 1)
brownian_bridge = brownian_paths - t * brownian_paths[-1]

print(f"Std de W(1): {brownian_paths[-1].std():.4f}")
print(f"Std del puente en t ≈ 0.5: {brownian_bridge[n_steps // 2].std():.4f}")
















fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 9))

ax1.plot(t, brownian_paths)
ax1.set_title("Brownian Motion")
ax1.set_xlabel("t")
ax1.set_ylabel("W(t)")
ax1.grid(True)

ax2.plot(t, brownian_bridge)
ax2.set_title("Brownian Bridge")
ax2.set_xlabel("t")
ax2.grid(True)
ax2.sharey(ax1)

ax3.hist(brownian_paths[-1], bins=20, density=True, alpha=0.7)
ax3.set_title("Distribución de B(1)")
ax3.set_xlabel("Valor")
ax3.set_ylabel("Densidad")
ax3.grid(True)

ax4.hist(
    brownian_bridge[n_steps // 2],
    bins=100,
    density=True,
    alpha=0.7
)
ax4.set_title("Distribución del puente en t=0.5")
ax4.set_xlabel("Valor")
ax4.grid(True)

plt.tight_layout()
plt.show()