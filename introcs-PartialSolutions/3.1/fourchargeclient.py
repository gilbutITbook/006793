#-----------------------------------------------------------------------
# fourchargeclient.py
#-----------------------------------------------------------------------

import sys
import stdio
from charge import Charge

# Accept a float w as a command-line argument. Create four Charge
# objects that are each distance w in each of the four cardinal
# directions from (.5, .5), and write the potential at (.25, .5).

w = float(sys.argv[1])

# Center of standard drawing window.
cx = 0.5
cy = 0.5

# Construct four charges.
c1 = Charge(cx + w, cy,     1.0);    # east
c2 = Charge(cx,     cy - w, 1.0);    # south
c3 = Charge(cx - w, cy,     1.0);    # west
c4 = Charge(cx,     cy + w, 1.0);    # north

# Compute potentials at (.25, .5).
px = 0.25
py = 0.5
v1 = c1.potentialAt(px, py)
v2 = c2.potentialAt(px, py)
v3 = c3.potentialAt(px, py)
v4 = c4.potentialAt(px, py)

# Compute and output total potential.
total = v1 + v2 + v3 + v4
stdio.writeln('total potential = ' + str(total))

#-----------------------------------------------------------------------

# python fourchargeclient.py 100
# total potential = 359600561.88465726

# python fourchargeclient.py 500
# total potential = 71920004.4950031

