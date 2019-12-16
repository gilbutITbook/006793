#-----------------------------------------------------------------------
# drunks.py
#-----------------------------------------------------------------------

import sys
import stdrandom
import stddraw
import stdarray
from turtle import Turtle

# Accept as command-line arguments an integer turtleCount, an integer
# stepCount, and a float stepSize. Create turtleCount Turtle objects,
# and have them make stepCount random steps of size stepSize.

turtleCount = int(sys.argv[1])
stepCount = int(sys.argv[2])
stepSize = float(sys.argv[3])
stddraw.setPenRadius(0.0)
stddraw.clear(stddraw.LIGHT_GRAY)
turtles = stdarray.create1D(turtleCount)
for i in range(turtleCount):
    x = stdrandom.uniformFloat(0.0, 1.0)
    y = stdrandom.uniformFloat(0.0, 1.0)
    turtles[i] = Turtle(x, y, 0.0)
for j in range(stepCount):
    for i in range(turtleCount):
        turtles[i].turnLeft(stdrandom.uniformFloat(0.0, 360.0))
        turtles[i].goForward(stepSize)
        stddraw.show(0.0)
stddraw.show()
    
#-----------------------------------------------------------------------

# python drunks.py 20 500 .005

# python drunks.py 20 1000 .005

# python drunks.py 20 5000 .005
