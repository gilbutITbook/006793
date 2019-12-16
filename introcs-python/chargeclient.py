#-----------------------------------------------------------------------
# chargeclient.py
#-----------------------------------------------------------------------

import sys
import stdio
from charge import Charge

# Accept floats x and y as command-line arguments. Create two Charge
# objects with fixed position and electrical charge, and write to
# standard output the potential at (x, y) due to the two charges.

x = float(sys.argv[1])
y = float(sys.argv[2])
c1 = Charge(.51, .63, 21.3)
c2 = Charge(.13, .94, 81.9)
v1 = c1.potentialAt(x, y)
v2 = c2.potentialAt(x, y)
stdio.writef('potential at (%.2f, %.2f) due to\n', x, y)
stdio.writeln('  ' + str(c1) + ' and')
stdio.writeln('  ' + str(c2))
stdio.writef('is %.2e\n', v1+v2)

#-----------------------------------------------------------------------

# python chargeclient.py .2 .5
# potential at (0.20, 0.50) due to
#   21.3 at (0.51, 0.63) and
#   81.9 at (0.13, 0.94)
# is 2.22e+12

# python chargeclient.py .51 .94
# potential at (0.51, 0.94) due to
#   21.3 at (0.51, 0.63) and
#   81.9 at (0.13, 0.94)
# is 2.56e+12

