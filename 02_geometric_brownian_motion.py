import numpy as np 
import matplotlib.pyplot as plt
m = 100
n = 1000
Zt = np.random.normal(0,1,(n,m))
dt = 1/n  
sigma = 0.4 # volatility (annualized standard deviation)
# Geometric Brownian Motion:
# S[i] = S[i-1] + mu*S[i-1]*dt + sigma*S[i-1]*sqrt(dt)*Z[i]
mu = 0.1 # drift (annual growth rate of assets)
S = np.zeros((n,m))
S[0] = 82.04 # initial asset price
for i in range (1,n):
    S[i] = S[i-1] + mu*S[i-1]*dt + sigma*S[i-1]*np.sqrt(dt)*Zt[i] #Euler-Maruyama solution
t = np.linspace(0, 1, n)
plt.plot(t, S)
plt.grid(True)
plt.title("Geometric Brownian Motion - Stock Price")
plt.xlabel("Paso temporal")
plt.ylabel("S(t)")
plt.show()
plt.hist(S[-1], bins=40)
plt.grid(True)
plt.title("Distribución de precios finales")
plt.xlabel("S(1)")
plt.ylabel("Frecuencia")
plt.show()

final_prices = S[-1]
mean_final = np.mean(final_prices)
median_final = np.median(final_prices)
p5 = np.percentile(final_prices, 5)
p95 = np.percentile(final_prices, 95)
prob_loss = np.mean(final_prices < S[0, 0])
prob_gain = np.mean(final_prices > S[0, 0])

print("Monte Carlo summary")
print("-------------------")
print(f"Initial price: {S[0,0]:.2f}")
print(f"Mean final price: {mean_final:.2f}")
print(f"Median final price: {median_final:.2f}")
print(f"5th percentile: {p5:.2f}")
print(f"95th percentile: {p95:.2f}")
print(f"Probability of loss: {prob_loss:.2%}")
print(f"Probability of gain: {prob_gain:.2%}")
print(f"Precio maximo: {np.max(final_prices):.2f}")
print(f"Precio minimo: {np.min(final_prices):.2f}")

