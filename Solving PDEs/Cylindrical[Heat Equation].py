# Task 4
import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits import mplot3d

# define the number pi
pi = np.pi

# define the radius
a = 1
# define T0
T0 =50

# define r range (i.e. 0 to a in step 0.1)
r = np.arange(0,a,0.01)
# define theta range (i.e. 0 to pi in step 0.1)
theta = np.arange(0,pi,0.01)
# now create two grids, i.e. two two-dimensional arrays, to represent all the x and all teh y values
(Rg, Thetag) = np.meshgrid(r,theta)

# trasform polar coordinate in Cartesian for plotting purposes only
(Xg,Yg) = (Rg*np.cos(Thetag),Rg*np.sin(Thetag))
    
# find the size of the grid
S = Rg.shape

# set the number of terms
RN = range(5,105,10)

for N in RN:
    # compute the function f with N terms in the series
    
    # set the range of the series, from 1 to N (included) with odd values only
    Rn = range(1,N+1,2)
    
    # initialise the two dimensional array for f
    f = np.zeros((S[0],S[1]))
    
    for n in Rn:
        # add the term n-th
        f = f + 4*T0/pi*((Rg/a)**n)/n * np.sin(n*Thetag)
        
        
    # plot surface or contour plot, in the same figure, next to each others
    ax = pl.axes(projection='3d')
    ax.plot_surface(Xg,Yg,f)
    #pl.contour(Xg,Yg,f,20)
    pl.show()