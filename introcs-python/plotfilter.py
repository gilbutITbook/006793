#-----------------------------------------------------------------------
# plotfilter.py
#-----------------------------------------------------------------------

import stdio
import stddraw

# Read x and y scales from standard input, and configure standard
# draw accordingly. Then read points from standard input until
# end-of-file, and plot them on standard draw.

x0 = stdio.readFloat()
y0 = stdio.readFloat()
x1 = stdio.readFloat()
y1 = stdio.readFloat()

stddraw.setXscale(x0, x1)
stddraw.setYscale(y0, y1)

# Read and plot the points.
stddraw.setPenRadius(0.0)
while not stdio.isEmpty():
    x = stdio.readFloat()
    y = stdio.readFloat()
    stddraw.point(x, y)

stddraw.show()

#-----------------------------------------------------------------------

# python plotfilter.py < usa.txt

