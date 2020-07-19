#Task A: Simpson Integration & Adaptive Simpson Integration

def Simpson(h,y):
    # number of nodal pointa
    N = len(yn)
    # initialise sum
    S = 0
    # loop every two points, and use the three points for Simpson rule
    # current point yn[i] and successive two points yn[i+1], yn[i+2]
    for i in range(0,N-2,2):
        S += h/3 * ( yn[i] + 4*yn[i+1] + yn[i+2] )
    return S
    
#alternate method
#def Simpson(h,y):
#    N = len(y) - 1
#    I = (h/3)*(y[0] + y[N-1] + 4*(np.sum(y[1:N-1:2]))+2*(np.sum(y[2:N-2:2])))
#    return I    
    


#ADAPTIVE SIMPSON using recursive
M =1
xn = np.linspace(0,4,M+1)
yn = np.sin(xn)
h = xn[1]-xn[0]
i = Simpson(h,yn)

def Adaptive_Int(M,y):
    er_min = 1.0e-5
    x = np.linspace(0,4,M+1)
    y = np.sin(x)
    h = x[1] - x[0]
    
    I = Simpson(h,y)
    er_actual = (1/15)*(Simpson(h/2,y) - I)
    
    if er_actual <= er_min:
        return I
    else:
        Adaptive_Int(2*(M),y)




# adaptive Simpson

# set a desired tolerance
tol = 1.0e-5
# set the domain of integration
a = 0
b = 4

# start with minimal number of sub intervals: one
# M is number of subintervals
M = 1
# determine the the nodal points for the present interval
xn = np.linspace(a,b,M+1)
yn = f(xn)
# determine the size of the interval
h = xn[1] - xn[0]
# compute integral with Simpson rule
S = Simpson(h,yn)
# set a fake error larger than the tolerance, to enter the while loop
err = tol * 10
# keep reducing the interval size if tolerance not reached
while err >= tol:
    # half the size of subintervals
    M = 2 * M
    # determine the the nodal points for the present intervals
    xn = np.linspace(a,b,M+1)   
    yn = f(xn)
    # determine the size of the intervals
    h = xn[1] - xn[0]
    # compute integral with Simpson rule
    Shalf = Simpson(h,yn)
    # compute the error, between present half size and previous size
    err = 1/15*np.abs(Shalf - S)
    # set current size as previous
    S = Shalf

    
print('Integral: ',S)
print('Number of nodes reached: ',M+1)
print('Error achieved: ',err)