#-----------------------------------------------------------------------
# charge.py
#-----------------------------------------------------------------------

import sys
import math
import stdio

#-----------------------------------------------------------------------

class Charge:

    # Construct self centered at (x, y) with charge q.
    def __init__(self, x0, y0, q0):
        self._rx = x0  # x value of the query point
        self._ry = y0  # y value of the query point
        self._q = q0   # Charge

    # Return the potential of self at (x, y).
    def potentialAt(self, x, y):
        COULOMB = 8.99e09
        dx = x - self._rx
        dy = y - self._ry
        r = math.sqrt(dx*dx + dy*dy)
        if r == 0.0: # Avoid division by 0
            if self._q >= 0.0:
                return float('inf')
            else:
                return float('-inf')
        return COULOMB * self._q / r

    # Return a string representation of self.
    def __str__(self):
        result = str(self._q) + ' at ('
        result += str(self._rx) + ', ' + str(self._ry) + ')'
        return result

#-----------------------------------------------------------------------

# For testing.
# Accept floats x and y as command-line arguments. Create a Charge
# objects with fixed position and electrical charge, and write to
# standard output the potential at (x, y) due to the charge.

def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    c = Charge(.51, .63, 21.3)
    stdio.writeln(c)
    stdio.writeln(c.potentialAt(x, y))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python charge.py .5 .5
# 21.3 at (0.51, 0.63)
# 1468638248194.164

