#-----------------------------------------------------------------------
# turtle.py
#-----------------------------------------------------------------------

import sys
import math
import stddraw

#-----------------------------------------------------------------------

class Turtle:

    # Construct self at (x, y) facing angle degrees counterclockwise
    # from the x-axis.
    def __init__(self, x, y, angle):
        self._x = x          # x-coordinate of turtle in unit square
        self._y = y          # y-coordinate of turtle in unit square
        self._angle = angle  # orientation of turtle (degrees,
                             # counterclockwise from x-axis)

    # Rotate self counterclockwise delta degrees.
    def turnLeft(self, delta):
        self._angle += delta

    # Move self forward. The distance traversed is defined by step.
    # Draw a line while moving.
    def goForward(self, step):
        oldx = self._x
        oldy = self._y
        self._x += step * math.cos(math.radians(self._angle))
        self._y += step * math.sin(math.radians(self._angle))
        stddraw.line(oldx, oldy, self._x, self._y)

#-----------------------------------------------------------------------

# For testing.
# Accept integer n from the command-line. Draw a polygon
# with n sides to stddraw.

def main():
    n = int(sys.argv[1])
    turtle = Turtle(.5, .0, 180.0/n)
    stepSize = math.sin(math.radians(180.0/n))
    stddraw.clear(stddraw.LIGHT_GRAY)
    for i in range(n):
        turtle.goForward(stepSize)
        turtle.turnLeft(360.0/n)
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# Example executions:

# python turtle.py 3
# python turtle.py 7
# python turtle.py 30
