#-----------------------------------------------------------------------
# koch.py
#-----------------------------------------------------------------------

import sys
import stddraw
from turtle import Turtle

# Plot to stddraw a Koch curve of order n, with step size stepSize,
# using Turtle object myTurtle.

def koch(n, stepSize, myTurtle):
    if n == 0:
        myTurtle.goForward(stepSize)
        return  
    koch(n-1, stepSize, myTurtle)
    myTurtle.turnLeft(60.0)
    koch(n-1, stepSize, myTurtle)
    myTurtle.turnLeft(-120.0)
    koch(n-1, stepSize, myTurtle)
    myTurtle.turnLeft(60.0)
    koch(n-1, stepSize, myTurtle)
 
# Accept integer n as a command-line argument. Plot a Koch curve of 
# order n to standard draw.

n = int(sys.argv[1])
stddraw.setCanvasSize(512, 256)
stddraw.setYscale(-.1, 0.4)
stddraw.setPenRadius(0.0)
stddraw.clear(stddraw.LIGHT_GRAY)
stepSize = 1.0 / (3.0 ** n)
myTurtle = Turtle(0.0, 0.0, 0.0)
koch(n, stepSize, myTurtle)
stddraw.show()

#-----------------------------------------------------------------------

# python koch.py 0

# python koch.py 1

# python koch.py 2

# python koch.py 3

# python koch.py 4

