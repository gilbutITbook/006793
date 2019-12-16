#-----------------------------------------------------------------------
# closest.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept three float command-line arguments x, y, z. Read from standard
# input a sequence of point coordinates (xi, yi, zi), and write to
# standard output the coordinates of the point closest to (x, y, z).

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if stdio.isEmpty():
    stdio.writeln('No points provided')
    sys.exit()

bestDist2 = float('inf')

while not stdio.isEmpty():
    xi = stdio.readFloat()
    yi = stdio.readFloat()
    zi = stdio.readFloat()
    dist2 = (x - xi) * (x - xi) + (y - yi) * (y - yi) + \
            (z - zi) * (z - zi)
    if dist2 < bestDist2:
        bestx = xi
        besty = yi
        bestz = zi
        bestDist2 = dist2

# Write the results.
stdio.writef('Closest point = (%f, %f, %f)\n', bestx, besty, bestz)

#-----------------------------------------------------------------------
#
# python closest.py 1.0 5.0 2.0
# 1.0 3.0 9.0
# 5.0 3.0 2.5
# 9.0 6.0 2.0
# 2.0 6.0 3.0
# 5.0 6.0 5.0
# Closest point = (2.000000, 6.000000, 3.000000)

