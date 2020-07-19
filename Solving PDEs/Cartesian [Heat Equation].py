import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits import mplot3d

# define the number pi
pi = np.pi

# define x range (i.e. 0 to 2 in step 0.1)
x = np.arange(0,2,0.1)
# define y range (i.e. 0 to 4 in step 0.1)
y = np.arange(0,4,0.1)
# now create two grids, i.e. two two-dimensional arrays, to represent all the x and all the y values
(Xg, Yg) = np.meshgrid(x,y)
# find the size of the grid
S = Xg.shape


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
        f = f + 40/pi*(np.sinh(n*pi/4*(Xg-2)))/(n*np.sinh(-n*pi/2))*np.sin(n*pi*Yg/4)
    
    # plot this result, with N terms
    ax = pl.axes(projection='3d')
    ax.plot_surface(Xg,Yg,f)
    pl.show()