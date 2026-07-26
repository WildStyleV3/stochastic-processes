import numpy as np
import matplotlib.pyplot as plt

# ¿Qué ocurre cuando ese ruido afecta proporcionalmente a una variable que
# además tiene una tendencia de crecimiento o decrecimiento?
#El GBM modela cambios proporcionales del precio. Euler–Maruyama 
# aproxima su dinámica paso a paso, 
# mientras que la solución exacta utiliza la forma exponencial 
# y conserva la distribución lognormal y la positividad

m = 500
n = 1000
T = 10

Zt = np.random.normal(0, 1, (n, m))
dt = T / (n - 1)

sigma = 0.15  # volatilidad anual
mu = 0.1      # crecimiento promedio anual

# Euler-Maruyama
S_euler = np.zeros((n, m))
S_euler[0] = 100

# Solución exacta del GBM
S_exact = np.zeros((n, m))
S_exact[0] = 100

for i in range(1, n):
    # Euler-Maruyama
    S_euler[i] = S_euler[i-1] + mu*S_euler[i-1]*dt + sigma*S_euler[i-1]*np.sqrt(dt)*Zt[i]

    # Solución exacta del GBM
    S_exact[i] = S_exact[i-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Zt[i])

t = np.linspace(0, T, n)

# Trayectorias
for j in range(500):
    line, = plt.plot(
        t,
        S_euler[:, j],
        alpha=0.7,
        label="Euler-Maruyama" if j == 0 else "_nolegend_"
    )

    plt.plot(
        t,
        S_exact[:, j],
        "--",
        color=line.get_color(),
        alpha=0.9,
        label="Solución exacta" if j == 0 else "_nolegend_"
    )

plt.grid(True)
plt.title("GBM: Euler-Maruyama vs solución exacta")
plt.xlabel("Tiempo")
plt.ylabel("S(t)")
plt.legend()
plt.show()

# Histogramas finales
plt.hist(S_euler[-1], bins=40, density=True, alpha=0.5, label="Euler-Maruyama")
plt.hist(S_exact[-1], bins=40, density=True, alpha=0.5, label="Solución exacta")
plt.grid(True)
plt.title("Distribución de precios finales")
plt.xlabel("S(10)")
plt.ylabel("Densidad")
plt.legend()
plt.show()

# Resumen Monte Carlo
final_euler = S_euler[-1]
final_exact = S_exact[-1]

print("Monte Carlo summary - Euler-Maruyama")
print("------------------------------------")
print(f"Initial price: {S_euler[0,0]:.2f}")
print(f"Mean final price: {np.mean(final_euler):.2f}")
print(f"Median final price: {np.median(final_euler):.2f}")
print(f"5th percentile: {np.percentile(final_euler, 5):.2f}")
print(f"95th percentile: {np.percentile(final_euler, 95):.2f}")
print(f"Probability of loss: {np.mean(final_euler < S_euler[0,0]):.2%}")
print(f"Probability of gain: {np.mean(final_euler > S_euler[0,0]):.2%}")
print(f"Precio máximo: {np.max(final_euler):.2f}")
print(f"Precio mínimo: {np.min(final_euler):.2f}")

print()
print("Monte Carlo summary - Solución exacta")
print("-------------------------------------")
print(f"Initial price: {S_exact[0,0]:.2f}")
print(f"Mean final price: {np.mean(final_exact):.2f}")
print(f"Median final price: {np.median(final_exact):.2f}")
print(f"5th percentile: {np.percentile(final_exact, 5):.2f}")
print(f"95th percentile: {np.percentile(final_exact, 95):.2f}")
print(f"Probability of loss: {np.mean(final_exact < S_exact[0,0]):.2%}")
print(f"Probability of gain: {np.mean(final_exact > S_exact[0,0]):.2%}")
print(f"Precio máximo: {np.max(final_exact):.2f}")
print(f"Precio mínimo: {np.min(final_exact):.2f}")