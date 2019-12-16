#-----------------------------------------------------------------------
# horner.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys
import math

#-----------------------------------------------------------------------

# Use Horner's method to compute and return the polynomial
#    a[0] + a[1] x^1 + a[2] x^2 + ... + a[n-1] x^(n-1)
# evaluated at x.

def evaluate(x, a):
    result = 0
    for i in range(len(a)-1, -1, -1):
        result = a[i] + (x * result)
    return result

#-----------------------------------------------------------------------

# Accept integer command-line argument n, compute n terms
# of the Taylor series e^x = 1 + x + x^2/2! + .... Then read
# values x from standard input, and write to standard output the
# polynomial evaluated at x. Also write to standard output the
# value computed by math.exp(x).

n = int(sys.argv[1])

# Compute coeffients for Taylor series
# e^x = 1 + x + x^2/2! + x^3/3! + ...
a = stdarray.create1D(n, 0.0)
a[0] = 1.0
for i in range(1, n):
    a[i] = a[i-1] / float(i)

# Evaluate the polynomial at values x read from standard input.
while not stdio.isEmpty():
    x = stdio.readFloat()
    stdio.writeln(evaluate(x, a))
    stdio.writeln(math.exp(x))
    stdio.writeln()

#-----------------------------------------------------------------------

# python horner.py 30
# 0
# 1.0
# 1.0
# 
# 1
# 2.718281828459045
# 2.718281828459045
# 
# 2
# 7.38905609893065
# 7.38905609893065
# 
# .5
# 1.6487212707001282
# 1.6487212707001282
# 
# -.1
# 0.9048374180359595
# 0.9048374180359595
# 
