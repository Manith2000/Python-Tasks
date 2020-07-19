#Solving Predator-prey problem (case study: London rental market)
import numpy as np
#Implement Explicit Method Forward EUler
# System of two ODEs with Forward Euler
def FwEulerTwo(Y0,t0,tend,h):
    # compose nodal times
    t = np.arange(t0,tend+h,h)
    # determine the number of time steps
    N = len(t)
    # allocate output array
    Y = np.ndarray((2,N))
    # initialise the solution
    t[0] = t0
    Y[0,0] = Y0[0]
    Y[1,0] = Y0[1]
    # compute the solution incrementally at subsequent time steps
    for n in range(1,N):
        Y[0,n] = Y[0,n-1] + func1(t[n-1],Y[:,n-1]) * h
        Y[1,n] = Y[1,n-1] + func2(t[n-1],Y[:,n-1]) * h
    return (t,Y)

# set the initial coditions for predator-prey problem
Y0 = np.ndarray(2)
Y0[0] = 0.8 # rental price  (in k£)
Y0[1] = 7 # number of inhabitants (in millions)

# remember to set F1 and F2 in func1 and func2
(t,Y) = FwEulerTwo(Y0,0,40,0.019)
pl.plot(t,Y[0,:])
pl.plot(t,Y[1,:])
pl.legend(['£','N'])
pl.show()

pl.plot(Y[0,:],Y[1,:])

