# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:12:58 2019

@author: mla18
"""


import matplotlib.pyplot as plt
import numpy as np

# DIVERGENCE & CURL

#TASK NO. 1: SKETCHING A FUNCTION
dx = 0.1
dy = 0.1

#create a 2D grid
x = np.arange(-5,5,dx)
y = np.arange(-5,5,dy)
Xg, Yg = np.meshgrid(x,y)

#allocate an array for function F which is just Nx by Ny by 2 (2 because its a 2D function)
F = np.ndarray((len(x),len(y),2))
#since we are using grids i/e/ vectoried form we can write formulas like in maths
#i component: slice only first layer and assign values for all x and y
F[:,:,0] = Yg/ (Xg**2 + Yg**2)
#j component: slice only second layer and assign values for all x and y
F[:,:,1] = -Xg/(Xg**2 + Yg**2)

#Xg and Yg are the independent domain
#F[:,:,0] and F[:,:,1] are two components

#this is how we compute PARTIAL derivaties using forward derivative scheme
#notice how there is one fewer column and row due to forward scheme
DivF = ((F[0])-1,(F[1])-1) #notice how there isnt 2 dimensions since divF is a scalar field

DivF = ( (F[:-1,1:,0]-F[:-1,:-1,0])/(Xg[:-1,1:]-Xg[:-1,:-1]) ) + \
       ( (F[1:,:-1,1]-F[:-1,:-1,1])/(Yg[1:,:-1]-Yg[:-1,:-1]) )
#set 3d axes
from mpl_toolkits import mplot3d
ax = plt.axes(projection='3d')

# plot surface divf vs x and y
ax.plot_surface(Xg[:-1,:-1],Yg[:-1,:-1],DivF)
#plot contour
plt.contour(Xg[:-1,:-1],Yg[:-1,:-1],DivF)




