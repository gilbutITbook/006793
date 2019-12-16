#-----------------------------------------------------------------------
# spirograph.py
#-----------------------------------------------------------------------

import stddraw
import sys
import math

# Accept float command-line arguments R, r, and a.
# Draw a curve formed by rolling a smaller circle of radius r inside
# a larger circle or radius R. If the pen offset of the pen point in
# the moving circle is a, then the equation of the resulting curve
# at time t is
#
# x = (R+r)*cos(t) - (r+a)*cos(((R+r)*t)/r)
# y = (R+r)*sin(t) - (r+a)*sin(((R+r)*t)/r)
 
# Credits: idea suggested by Diego Nehab
# Reference: http://www.math.dartmouth.edu/~dlittle/java/SpiroGraph
# Reference: http://www.wordsmith.org/~anu/java/spirograph.html

R = float(sys.argv[1])
r = float(sys.argv[2])
a = float(sys.argv[3])

stddraw.setXscale(-300, +300)
stddraw.setYscale(-300, +300)
stddraw.setPenRadius(0.0)

t = 0.0
while True:
    x = (R+r) * math.cos(t) - (r+a) * math.cos(((R+r)*t)/r)
    y = (R+r) * math.sin(t) - (r+a) * math.sin(((R+r)*t)/r)
    degrees = -math.degrees((R+r)/r)*t
    stddraw.point(x, y)
    #stddraw.picture(x, y, "earth.gif", degrees)
    #stddraw.rotate(+Math.toDegrees((R+r)/r)*t)
    stddraw.show(10.0)
    t += 0.01

#-----------------------------------------------------------------------

# python spirograph.py 180 40 15

# python spirograph.py 100 55 20
 
