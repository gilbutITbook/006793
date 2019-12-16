#-----------------------------------------------------------------------
# gaussian.py
#-----------------------------------------------------------------------

import sys
import stdio
import math

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean mu
# and standard deviation sigma at the given x value.

def pdf(x, mu=0.0, sigma=1.0):
    x = float(x - mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean mu and standard deviation sigma at the given z value.

def cdf(z, mu=0.0, sigma=1.0):
    z = float(z - mu) / sigma
    if z < -8.0: return 0.0
    if z > +8.0: return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / i
        i += 2
    return 0.5 + total * pdf(z)

#-----------------------------------------------------------------------

# Accept floats z, mu, and sigma as command-line arguments. Use them
# to test the phi() and Phi() functions. Write the
# results to standard output.

def main():
    z = float(sys.argv[1])
    mu = float(sys.argv[2])
    sigma = float(sys.argv[3])

    stdio.writeln(cdf(z, mu, sigma))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python gaussian.py 820 1019 209
# 0.17050966869132106

# python gaussian.py 1500 1019 209
# 0.9893164837383885

# python gaussian.py 1500 1025 231
# 0.9801220907365491
