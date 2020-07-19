import numpy as np

R = 5 # set radius of the domain

# set the step intervals in x and y
dx = 0.05
dy = 0.05

# set the x range, not including the boundaries
x = np.arange(-R+dx,R,dx)
N = len(x)
# the y range depends of the various values of x, and cannot be fixed here

# integrate in dy, for all the value of x, i.e. find G(x)

G = np.zeros(N)
# for every x
for i in range(0,N):
    # determine the boundaries m and p for this x
    mx = np.sqrt(R**2-x[i]**2)
    px = mx
    # set the y points for this x, not including the boundaries
    y = np.arange(-mx+dy,px,dy)
    z = np.zeros(len(y))
    # determine the values of the function z(x,y)
    for j in range(0,len(y)):
        z[j] = np.sqrt(R-np.sqrt(x[i]**2+y[j]**2)) # dome of Samarkand
        # z[j] = np.sqrt(R**2-x[i]**2-y[j]**2) # emisphere
    
    # integrate in dy from cx to dx (for this specific x)
    G[i] = trapzeqd(y,z) # G(x)

# integrate G(x) in dx
I = trapzeqd(x,G)

print(I)

# for an emisphere the volume is:
#print(4/3*np.pi*R**3/2)