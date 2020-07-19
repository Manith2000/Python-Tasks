import numpy as np
import matplotlib.pyplot as pl

# Input data
# spatial domain
a = 0  # lower boundary
b = 0.5 # upper boundary
dx = 0.01 # spatial increment
# temporal domain
tend = 3600 # temporal span
dt = 1 # temporal increment

# set the physics
# boundary conditions (fixed temperature at boundaries)
Ta = 50 
Tb = 70
# initial condition (initial temperature of the bar)
T0 = 10 # initial temperature

alpha = 1.172e-5 # thermal diffusivity
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

# compute the constant coefficient
c = alpha * dt / dx**2

# compute the solution incrementally at subsequent time steps
for p in range(1,Nt):
    # compute at time step p, i.e. t = p * dt
    # do it for every node in the spatial grid
    # start with the boundaries
    T[p,0] = Ta
    T[p,Nx-1] = Tb
    # do the interior nodes
    for i in range(1,Nx-1):#note how we ignore the final x value since we know boundary conditions
        # apply the discretised equation
        T[p,i] = c * ( T[p-1,i+1] + T[p-1,i-1] ) + (1 - 2*c) * T[p-1,i]
#IMPORTANT : note how we put -1 for time discretisation since we already knew the initial condition
pl.plot(x,T[-1,:])