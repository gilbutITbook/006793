#-----------------------------------------------------------------------
# bisection.py
#-----------------------------------------------------------------------

import sys
import stdio
import gaussian

#-----------------------------------------------------------------------

# Return a float within the interval (lo, hi) for which f(x) is equal
# to y within precision delta.

def invert(f, y, lo, hi, delta=0.00000001):
    mid = (lo + hi) / 2.0
    if (hi - lo) < delta:
        return mid
    if f(mid) > y:
        return invert(f, y, lo, mid, delta)
    else:
        return invert(f, y, mid, hi, delta)
        
#-----------------------------------------------------------------------

# Accept float command-line argument y. Compute and write to 
# standard output the value of x for which gaussian.cdf(x) = y.

def main(): 
    y = float(sys.argv[1])
    x = invert(gaussian.cdf, y, -8.0, 8.0)
    stdio.writef('%.3f\n', x)
    
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------  

# python bisection.py .5
# 0.000

# python bisection.py .95
# 1.645

# python bisection.py .975
# 1.960

