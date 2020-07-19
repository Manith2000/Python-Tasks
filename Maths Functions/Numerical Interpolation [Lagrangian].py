import numpy as np 
import matplotlib.pyplot as plt
def Lagrangian(j,xp,xn):
    L = 1
    r = range(0,len(xn))
    for i in r:
        if i != j:
            L = L*(xp - xn[i])/(xn[j]-xn[i])
    return L

x = np.arange(0,3.05,0.05)
y = np.sin(x)
r = range(2,5)

for k in r:
    xn = np.linspace(1,2,k)
    yn = np.sin(xn)
    p = []
    n = k - 1
    for xp in x:
        r1 = range(0,n+1)
        S = 0
        for j in r1:
            S += yn[j]*Lagrangian(j,xp,xn)
        p += [S]
    plt.plot(x,p)

# error analysis

a = 1 # lower interval
b = 2 # upper interval
xp = np.pi/2
y = []
for Nx in range(2,17):
    xn = np.linspace(a,b,Nx)
    yn = np.sin(xn)
    n = len(xn) - 1
    # interpolate for xp
    yp = 0
    # use Langrangian polynomial up to n, included
    for j in range(0,n+1):
        yp += yn[j] * Lagrangian(j,xp,xn)
    y += [yp]
# compute the basic error
y = np.array(y)
for i in range(0,14):
    error = y[i+1] - y[i]
    print(i+1,error)
    plt.scatter(i+1,np.log(error))
