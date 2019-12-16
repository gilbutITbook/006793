#-----------------------------------------------------------------------
# sqrt.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept float c as a command-line argument. Write to standard
# output the square root of c to 15 decimal places of accuracy.
# Use Newton's method.

EPSILON = 1e-15

c = float(sys.argv[1])
t = c
while abs(t - c/t) > (EPSILON * t):
    # Replace t by the average of t and c/t.
    t = (c/t + t) / 2.0
stdio.writeln(t)

#-----------------------------------------------------------------------

# python sqrt.py 2.0      
# 1.414213562373095

# python sqrt.py 2544545
# 1595.1630010754388
