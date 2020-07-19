# use forward difference

# allocate array for curl
CulrF = np.ndarray((Ny-1,Nx-1))
# if f = (f1)i + (f2)j
# curlf = (df2/dx-df1/dy)k
# df2/dx: traverse horizontal, i.e. second dimension/columns, for all rows, but last one. Use i component, ie layer 0
# df1/dy: traverse vertical, i.e. first dimension/rows, for all columns, but last one. Use j component, ie layer 1
CurlF = ( (F[:-1,1:,1]-F[:-1,:-1,1])/(Xg[:-1,1:]-Xg[:-1,:-1]) ) - \
         ((F[1:,:-1,0]-F[:-1,:-1,0])/(Yg[1:,:-1]-Yg[:-1,:-1]))

ax = pl.axes(projection='3d')
ax.plot_surface(Xg[:-1,:-1],Yg[:-1,:-1],CurlF)