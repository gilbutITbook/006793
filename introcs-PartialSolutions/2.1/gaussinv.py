#-----------------------------------------------------------------------
# gaussinv.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean 0.0
# and standard deviation 1.0 at the given x value.

def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean mu
# and standard deviation sigma at the given x value.

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean 0.0 and standard deviation 1.0 at the given z value.

def Phi(z):
    if z < -8.0:
        return 0.0
    if z > 8.0:
        return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2
    return 0.5 + phi(z) * total

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean mu and standard deviation sigma at the given z value.

def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)

#-----------------------------------------------------------------------

def _PhiInverse(y, delta, lo, hi):
    mid = lo + ((hi - lo) / 2.0)
    if (hi - lo) < delta:
        return mid
    if Phi(mid) > y:
        return _PhiInverse(y, delta, lo, mid)
    else:
        return _PhiInverse(y, delta, mid, hi)

#-----------------------------------------------------------------------

# Return x such that Phi(x) = y.

def PhiInverse(y):
    return _PhiInverse(y, .00000001, -8.0, 8.0)

#-----------------------------------------------------------------------

# For testing.

# Accept float z. Use it to test the PhiInverse() function. Write the
# results to standard output.

z = float(sys.argv[1])

y = Phi(z);
x = PhiInverse(y)
stdio.writeln(y);
stdio.writeln(x);

#-----------------------------------------------------------------------

# python gaussinv.py 1
# 0.841344746068543
# 1.0000000037252903

# python gaussinv.py 2
# 0.9772498680518207
# 2.0000000037252903

# python gaussinv.py 5
# 0.9999997133484283
# 5.00000000372529

# python gaussinv.py 8
# 0.9999999999999993
# 7.984248783439398

