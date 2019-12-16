#-----------------------------------------------------------------------
# checkerboard.py
#-----------------------------------------------------------------------

import stddraw
import sys

# Accept integer command-line argument n. Draw an n-by-n checkerboard.

n = int(sys.argv[1])

stddraw.setXscale(0, n)
stddraw.setYscale(0, n)

for i in range(n):
    for j in range(n):
        if ((i + j) % 2) != 0:
            stddraw.setPenColor(stddraw.BLACK)
        else:
            stddraw.setPenColor(stddraw.RED)
        stddraw.filledSquare(i + .5, j + .5, .5)

stddraw.show()

#-----------------------------------------------------------------------

# python checkerboard.py 8

