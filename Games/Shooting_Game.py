import random as rn
import math as mt
import matplotlib.pyplot as pl

def shootball(a0,v0,xt,yt,R):
    g = 9.81 # gravity
    dx = 0.01 # step
    shot = False
    # set lists x and y
    x = []
    y = []
    # set the initial point
    xp = 0
    yp = 0
    # keep moving the bullet until the target is hit, or the bullet reaches the ground
    while (not shot) and yp >= 0:
        # next x step
        xp += dx
        yp = xp*mt.tan(a0)-0.5*xp**2*g/(v0**2*mt.cos(a0)**2)
        # append new values to the lists
        x += [xp]
        y += [yp]   
        # check if the new point has hit the target
        if ( (xp-xt)**2 + (yp-yt)**2 ) <= R**2:
            shot = True
    return (x,y,shot)


# main script
R = 0.01 # radius of the target
# generate the target at random position
xt = rn.random()
yt = rn.random()
#xt = 0.9
#yt = 0.7
########
# generate the coordinates of the target
Rtheta = range(0,360)
xtarget = []
ytarget = []
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    xtarget += [R*mt.cos(thetar)+xt]
    ytarget += [R*mt.sin(thetar)+yt]
# plot teh target    
pl.scatter(xtarget,ytarget,s=2,c='r')
# set the axis to the unity quadrant
pl.axis([0, 1, 0, 1])
pl.show()
print('Shoot and hit me, if you dare!')

shot = False
# play the game, until target is shot
while not shot:
    # insert shooting angle and initial velocity
    theta0 = int(input('Shooting angle (in degree):'))
    theta0 = mt.pi/180*theta0
    v0 = input('Initial speed:')
    v0 = float(v0)
    # call the function
    (x,y,shot) = shootball(theta0,v0,xt,yt,R)
    # plot the war scenery
    pl.plot(x,y,'b',xtarget,ytarget,'r')
    pl.axis([0, 1, 0, 1])
    pl.show()
    if not shot:
        print('You missed the target. Try again')
        
print('Well done: target centred.')      