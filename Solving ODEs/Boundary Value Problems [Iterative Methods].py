import numpy as np
import matplotlib.pyplot as pl
def myfunc(x):
    
    # Tasks 1,2
    f = 2*x
    g = 2
    p = np.cos(3*x)

    # Task 3
    f = x
    g = 1
    p = 5*x

    # Task 4
    # nuclear rod
    K = 16.75
    R = 0.015
    f = 1 / x
    g = 0
    p = -10**8*np.exp(-x/R)/(x*K)
    
    return (f,g,p)
def Jacobi(a,b,ya,yb,N,tol):
    
    # define the range
    x = np.linspace(a,b,N+1)
    # find the interval
    h = x[1] - x[0]

    y = np.zeros(N+1)
    yk = np.zeros(N+1)
    
    c = 0
    err = 10.0 * tol
    while err > tol and c<100000:
    
        # enforce bc
        y[0] = ya
        y[N] = yb
        # evaluate internal points for next iteration
        for i in range(1,N):
            # solve for this x
            # evaluate the functions f, g and p at this x
            (f, g, p) = myfunc(x[i])
            y[i] = ( -(yk[i+1]+yk[i-1])/h**2 - f*(yk[i+1]-yk[i-1])/(2*h) + p ) / (g-2/h**2)

        err = np.max(np.abs(y - yk))
        yk = np.copy(y)
        c += 1
        
    print(c)
    return (x,y)
# Task 2
(x,y) = myodebc(0,np.pi,1.5,0,50)
pl.plot(x,y,'bo')
(x,y) = Jacobi(0,np.pi,1.5,0,50, 0.0001)
pl.plot(x,y,'rd')