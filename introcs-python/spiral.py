#-----------------------------------------------------------------------
# spiral.py
#-----------------------------------------------------------------------

import math
import sys
import stddraw
from turtle import Turtle

#-----------------------------------------------------------------------

# Accept command-line arguments n (an integer specifying a number
# of sides), wraps (an integer specifying a wrap count), and decay
# (a float specifying a decay factor). Draw to standard draw a spiral
# with those characteristics.

n = int(sys.argv[1])
wraps = int(sys.argv[2])
decay = float(sys.argv[3])

angle = 360.0 / n

step = math.sin(math.radians(angle/2.0))
turtle = Turtle(0.5, 0, angle/2.0)

stddraw.setPenRadius(0.0)
stddraw.clear(stddraw.LIGHT_GRAY)
for i in range(wraps * n):
    step /= decay
    turtle.goForward(step)
    turtle.turnLeft(angle)
stddraw.show()
    
#-----------------------------------------------------------------------

# python spiral.py 3 1 1.0

# python spiral.py 3 10 1.2

# python spiral.py 1440 10 1.0004

# python spiral.py 1440 10 1.00004
