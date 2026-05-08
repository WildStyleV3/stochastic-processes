import numpy as np 
import random 
import matplotlib.pyplot as plt
m = 100
n = 10000
y = np.zeros((n,m))
Zt = np.random.normal(0,1,(n,m))
dt = 1/n 
sigma = 2
#Brownian Motion
for i in range(1,n):
    y[i] = y[i-1]+ sigma*np.sqrt(dt)*Zt[i]
#Brownian Motion Bridge
t = np.linspace(0,1,n).reshape(n,1)
BB = y-t*y[-1]  
#plt.plot(y)
plt.plot(t,BB)
plt.grid(True)
plt.show()
plt.hist(y[-1], bins=30, density=True, alpha=0.7, label='Distribución de BM')
plt.title('Distribución de B(1)')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.legend()
plt.show()

