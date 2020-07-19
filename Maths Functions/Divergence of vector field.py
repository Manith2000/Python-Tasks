# use forward difference

# allocate array for divf: note that because we are performing derivative along y and x, we will have
# to renounce to the last row and last column
DivF = np.ndarray((Ny-1,Nx-1))
# if f = f1 * i + f2 * j
# divf = df1 / dx + df2 / dy
# df1/dx: scroll horizontal, i.e. in second dimension; for all rows, but the last one, 
# with first vector component, i.e. layer 0
# df2/dy: scroll vertical, i.e. infirst dimension; for all columns, but the last one, 
# with second vector component, i.e. layer 1
DivF = ( (F[:-1,1:,0]-F[:-1,:-1,0])/(Xg[:-1,1:]-Xg[:-1,:-1]) ) + \
       ( (F[1:,:-1,1]-F[:-1,:-1,1])/(Yg[1:,:-1]-Yg[:-1,:-1]) )

# plot results
# set 3D axes
from mpl_toolkits import mplot3d
ax = pl.axes(projection='3d')
# plot surface divf vs x and y
ax.plot_surface(Xg[:-1,:-1],Yg[:-1,:-1],DivF)

#pl.contour(Xg[:-1,:-1],Yg[:-1,:-1],DivF)