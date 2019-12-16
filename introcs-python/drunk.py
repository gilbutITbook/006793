#-----------------------------------------------------------------------
# drunk.py
#-----------------------------------------------------------------------

import sys
import stdrandom
import stddraw
from turtle import Turtle

#-----------------------------------------------------------------------

# Accept as command-line arguments an integer stepCount specifying a
# number of iterations, and a float stepSize specifying a step size.
# Create a Turtle object, and have it make stepCount random steps of
# size stepSize.

stepCount = int(sys.argv[1])
stepSize = float(sys.argv[2])
stddraw.setPenRadius(0.0)
stddraw.clear(stddraw.LIGHT_GRAY)
myTurtle = Turtle(0.5, 0.5, 0.0)
for i in range(stepCount):
    myTurtle.turnLeft(360.0 * stdrandom.uniformFloat(0.0, 360.0))
    myTurtle.goForward(stepSize)
    stddraw.show(0.0)
stddraw.show()

#-----------------------------------------------------------------------

# python drunk.py 10000 .01
