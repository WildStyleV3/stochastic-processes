import numpy as np 
import matplotlib.pyplot as plt 
#El GBM modela crecimiento proporcional sin capacidad de carga. 
# El crecimiento logístico estocástico agrega competencia, recursos limitados y saturación.
#Simular crecimiento logístico con capacidad de carga y ruido multiplicativo mediante Euler–Maruyama.
m = 200
n = 10000
T = 10
Zt = np.random.normal(0,1,(n,m))
dt = T / (n - 1) 
sigma = 0.1 #intensidad del ruido ambiental
r = 1 #velocidad de crecimiento
K = 100 #capacidad de carga
X = np.zeros((n,m))
X[0] = 10 #población inicial
for i in range(1,n):
    X[i] = (X[i-1]) + (r*X[i-1]*dt)*(1-X[i-1]/K) + sigma*X[i-1]*np.sqrt(dt)*Zt[i] 
t = np.linspace(0,T,n)
plt.plot(t, X[:, :30])
plt.grid(True)
plt.title("Stochastic Logistic Growth")
plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.show()
