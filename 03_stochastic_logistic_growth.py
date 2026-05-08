import numpy as np 
import matplotlib.pyplot as plt 
m = 200
n = 10000
T = 10
Zt = np.random.normal(0,1,(n,m))
dt = T/n  
sigma = 0.1
r = 1
K = 100
X = np.zeros((n,m))
X[0] = 10
for i in range(1,n):
    X[i] = (X[i-1]) + (r*X[i-1]*dt)*(1-X[i-1]/K) + sigma*X[i-1]*np.sqrt(dt)*Zt[i] 
t = np.linspace(0,T,n)
plt.plot(t,X)
plt.grid(True)
plt.title("Stochastic Logistic Growth")
plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.show()