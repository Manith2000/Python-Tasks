import matplotlib.pyplot as pl
import numpy as np
import math as mt
# This script solves the heat conduction equation with mixed boundary conditions


# set the input data
K = 100
S= 120
T = 3
r = 0.03
sigma = 1
# spatial domain
a = 0  # lower boundary
b = 50 # upper boundary
dx = 0.01 # spatial increment
# temporal domain
tend = 1000 # temporal span
dt = 1 # temporal increment

# set the physics
# initial condition (initial temperature of the bar)
T0 = K*(np.exp(np.log(S/K)+(r-0.5*(sigma**2))*T) - 1) # initial temperature

Tw = 5 # temperature of surrounding water
alpha = 0.5*(sigma**2) # thermal diffusivity
K = 40  # thermal conductivity
h = 500 # heat transfer coefficient
# ================================================

# greate the spatial grid points
x = np.arange(a,b+dx,dx)
Nx = len(x)
# create the temporal grid points
t = np.arange(0,tend+dt,dt)
Nt = len(t)

# create the solution matrix
T = np.ndarray((Nt,Nx))

# set the inital value everywhere along the bar
T[0,:] = T0
T[0,mt.ceil(Nx/2)] = 100 # set the sourse at the middle of the bar

# compute the constant coefficient
c = alpha * dt / dx**2

# compute the solution incrementally at subsequent time steps
for p in range(1,Nt):
    # compute at time step p, i.e. t = p * dt
    # do it for every node in the spatial grid
    # start with the boundaries
    T[p,0] = (h*Tw+K/dx*T[p-1,1]) / (h+K/dx)
    T[p,Nx-1] = (h*Tw+K/dx*T[p,Nx-2]) / (h+K/dx)
    # do the interior nodes
    for i in range(1,Nx-1):
        # apply the discretised equation
        T[p,i] = c * ( T[p-1,i+1] + T[p-1,i-1] ) + (1 - 2*c) * T[p-1,i]

    # enforce the source at the central node
    T[p,mt.ceil(Nx/2)] = 100


#pl.plot(x,T[0,:])
pl.plot(x,T[-1,:])

A = np.ndarray((2,2))
B = np.ndarray((3,2))
A[1,0]= 2
B[:,1] =3

print(np.matmul(A,B))