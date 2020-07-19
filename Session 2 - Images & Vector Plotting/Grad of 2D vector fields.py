# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:09:42 2019

@author: Manith Adikari
"""

import numpy as np
import matplotlib.pyplot as pl
dx = 0.1
dy = 0.1
x = np.arange(-10,10+dx,dx)
y = np.arange(-10,10+dy,dy)
n = len(x)
f = np.ndarray((n,n,2))
Xg,Yg = np.meshgrid(x,y)
f[:,:,0] = 14*Yg + Xg*4
f[:,:,1] = -11*Yg + -6*Xg

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
