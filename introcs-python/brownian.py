#-----------------------------------------------------------------------
# brownian.py
#-----------------------------------------------------------------------

import sys
import math
import stddraw
import stdrandom

#-----------------------------------------------------------------------

# Draw a Brownian bridge from (x0, y0) to (x1, y1) with the given
# variance and scaleFactor.

def curve(x0, y0, x1, y1, variance, scaleFactor):
    if (x1 - x0) < .01:
        stddraw.line(x0, y0, x1, y1)
        return
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    delta = stdrandom.gaussian(0, math.sqrt(variance))
    curve(x0, y0, xm, ym+delta, variance/scaleFactor, scaleFactor)
    curve(xm, ym+delta, x1, y1, variance/scaleFactor, scaleFactor)

#-----------------------------------------------------------------------

# Accept a Hurst exponent as a command-line argument.
# Use the Hurst exponent to compute a scale factor.
# Draw a Brownian bridge from (0, .5) to (1.0, .5) with
# variance .01 and that scale factor.

def main():
    hurstExponent = float(sys.argv[1])
    stddraw.setPenRadius(0.0)
    stddraw.clear(stddraw.LIGHT_GRAY)
    scaleFactor = 2 ** (2.0 * hurstExponent)
    curve(0, .5, 1.0, .5, .01, scaleFactor)
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python brownian.py 1

# python brownian.py .5

# python brownian.py .05
