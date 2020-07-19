import numpy as np
import matplotlib.pyplot as pl
# step
dx = 0.5
# set the range
x = np.arange(-10,10,dx)
# length of range
N = len(x)
# set grids
Xg , Yg = np.meshgrid(x,x)

# allocate array u
u = np.ndarray( (N,N,2) )
# set value for u: i and j components, for all x and y
u[:,:,0] = 4*Xg + 14*Yg
u[:,:,1] = -6*Xg - 11*Yg

# plot streamlines
pl.streamplot(Xg,Yg,u[:,:,0],u[:,:,1])
pl.show()


# compute the gradient
# allocate array for gradient: size will be N-1 by N-1 by 2 by 2
gradu = np.ndarray( (N-1,N-1,2,2) )


# temporary array for derivative
d = np.ndarray( (N-1,N-1) )
# compute individual terms of the grad matrix
for i in range(0,2):
    # compute derivative for component i of velocity: i=0 u component, i=1 v component
    for j in range(0,2):
        if j == 0:
            # derivative with respect to x: move horizontally, ie traverse columns
            g = (u[:-1,1:,i]-u[:-1,:-1,i]) / (x[1:] - x[:-1]) # note that x and y are the same
        else:
            # derivative with respect to y: move vertically, ie traverse rows
            g = (u[1:,:-1,i]-u[:-1,:-1,i]) / (x[1:] - x[:-1]) # note that x and y are the same
        
        # update the grad matrix 
        gradu[:,:,i,j] = g

# plot streamlines
# u component
pl.streamplot(Xg[:-1,:-1],Yg[:-1,:-1],gradu[:,:,0,0],gradu[:,:,0,1])
pl.show()
# v component
pl.streamplot(Xg[:-1,:-1],Yg[:-1,:-1],gradu[:,:,1,0],gradu[:,:,1,1])
pl.show()