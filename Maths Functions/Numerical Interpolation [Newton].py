import numpy as np 
import matplotlib.pyplot as pl

#recursive form
def NewtDivDiff(xn,yn):
    # recursive form
    
    # determine number of points
    N = len(xn)
    # set the order: 1 node -> f0; 2 nodes -> f1, etc.
    N = N - 1

    if N == 0:
        # f is the point itself
        f = yn[0]
    else:
        # f is defined recursively as (slide 64):
        # f = ( f[x0,...x(n-1)] - f[x1,...xn] ) / ( x0 - xn)
        f = ( NewtDivDiff(xn[:-1],yn[:-1]) - NewtDivDiff(xn[1:],yn[1:]) ) / ( xn[0] - xn[-1] )
    return f
#irrecursive form
def NewtDivDiffIt(xn,yn):
    # iterative form
    
    # determine number of points
    N = len(xn)
    # set the order: 1 node -> f0; 2 nodes -> f1, etc.
    N = N - 1
    f = np.copy(yn)
    for j in range(0,N):
        for i in range(0,N-j):
            f[i] = (f[i+1]-f[i]) / (xn[i+j+1]-xn[i])
             
    return f[0]



#Runges phenomenon 
# main
for m in range(2,16):    #no of nodes required
    a = -1 # lower interval
    b = 1 # upper interval
    xn = np.linspace(a,b,m)
    yn = 1/(1+25*(xn**2))
    # determine order
    k = m - 1  
    # set the domain of interpolation
    x = np.linspace(-1,1,50)
    y = []
    for xp in x:
        # determine pn at x = xp
        yp = yn[0]
        for i in range(0,k):
            prod = 1
            for j in range(0,i+1):
                prod *= (xp-xn[j])
    
            yp += prod * NewtDivDiff(xn[0:i+2],yn[0:i+2])
    
        y += [yp]
    
    # convert list into array
    y = np.array(y)   
    # plot polynomial in the interpolating range
    pl.plot(x,y,c='Red')
    # plot the actual function
pl.plot(x,1/(1+25*(x**2)),c='Orange')
pl.show()