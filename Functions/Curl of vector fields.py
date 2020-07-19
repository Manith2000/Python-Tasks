# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:15:13 2019

@author: mla18
"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt
#if 2D then curlf = ndarray((N,N)) since only k component

#/////////CURL OF A VECTOR FIELD //////////

# curl
# allocate array for curlf
curlf = np.ndarray((S[0]-1,S[1]-1,S[2]-1,3))
# compute the curl (with forward scheme)

# i component = df3/dy - df2/dz
curlf[:,:,:,0] = (f[1:,:-1,:-1,2]-f[:-1,:-1,:-1,2])/(Yg[1:,:-1,:-1]-Yg[:-1,:-1,:-1]) - \
                 (f[:-1,:-1,1:,1]-f[:-1,:-1,:-1,1])/(Zg[:-1,:-1,1:]-Zg[:-1,:-1,:-1])

# j component = df1/dz - df3/dx
curlf[:,:,:,1] = (f[:-1,:-1,1:,0]-f[:-1,:-1,:-1,0])/(Zg[:-1,:-1,1:]-Zg[:-1,:-1,:-1]) - \
                 (f[:-1,1:,:-1,2]-f[:-1,:-1,:-1,2])/(Xg[:-1,1:,:-1]-Xg[:-1,:-1,:-1])

# k component = df2/dx - df1/dy
curlf[:,:,:,2] = (f[:-1,1:,:-1,1]-f[:-1,:-1,:-1,1])/(Xg[:-1,1:,:-1]-Xg[:-1,:-1,:-1]) - \
                 (f[1:,:-1,:-1,0]-f[:-1,:-1,:-1,0])/(Yg[1:,:-1,:-1]-Yg[:-1,:-1,:-1])

#plotting
from mpl_toolkits import mplot3d
ax = pl.axes(projection='3d')
#remember to not include last Xg and Yg if forward diff derivative
ax.plot_surface(Xg[:-1,:-1],Yg[:-1,:-1],CurlF)

# the analytical solution is (z)i + (0)j + (0)k
print(curlf[:,:,:,0])
print(curlf[:,:,:,1])
print(curlf[:,:,:,2])


