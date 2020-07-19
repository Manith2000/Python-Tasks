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
#the following funciton is designed to accept different boundary conditions (dirichlet,mixed,neumann)
def myodebc2(a,b,bca,bcb,N,c):

    # define the range
    x = np.linspace(a,b,N+1)
    # find the interval
    h = x[1] - x[0]


    # build a set of algebraic equation A * y = b
    # where A is N+1 by N+1
    A = np.zeros((N+1,N+1))
    b = np.zeros(N+1)
    # set the boundary conditions
    # boundary a: we need the forward scheme
    A[0,0] = c[1] - c[0]/h
    A[0,1] = c[0]/h
    b[0] = bca
    
    # boundary b: we need the backward scheme
    A[N,N-1] = -c[2]/h
    A[N,N] = c[2]/h + c[3]
    b[N] = bcb

    # set equations for the interior points
    for i in range(1,N):
       # evaluate the functions f, g and p at this x
       (f, g, p) = myfunc(x[i])
       A[i,i-1] = 1/h**2 - f / (2*h)
       A[i,i] = g - 2 / h**2
       A[i,i+1] = 1/h**2 + f / (2*h)
       b[i] = p


    y = np.linalg.inv(A).dot(b)

    return (x,y)
(x,y) = myodebc2(0,2,0,-1,50,[1,0,1,0])
pl.plot(x,y,'bo')

#Case Study: Heat from a nuclear rod

# Task 4
# Nuclear rod

h = 6*10**4
K = 16.75
R = 0.015
w = 0.003
Tw = 473
Tw = 490
# 1
# set the b.c.
c = np.zeros(4)
# at boundary a
c[0] = 1
c[1] = 0
bca = -6.32*10**5 / K
# at boundary b
c[2] = 1
c[3] = h / K
bcb = h / K * Tw

(x,y) = myodebc2(R,R+w,bca,bcb,50,c)
pl.plot(x,y,'bo')