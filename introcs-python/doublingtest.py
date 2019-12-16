#-----------------------------------------------------------------------
# doublingtest.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stdio
import stdrandom
import threesum
from stopwatch import Stopwatch

#-----------------------------------------------------------------------

# Return the time to solve a random instance of the threesum problem
# of size n.

def timeTrial(n):
    a = stdarray.create1D(n, 0)
    for i in range(n):
        a[i] = stdrandom.uniformInt(-1000000, 1000000)
    watch = Stopwatch()
    count = threesum.countTriples(a)
    return watch.elapsedTime()

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard output
# a table of doubling ratios for the threesum problem of size n, n*2,
# n*4, etc.

n = int(sys.argv[1])
while True:
    previous = timeTrial(n // 2)
    current  = timeTrial(n)
    ratio = current / previous
    stdio.writef('%7d %4.2f\n', n, ratio)
    n *= 2

#-----------------------------------------------------------------------

# python doublingtest.py 256
#     256 7.82
#     512 8.34
#    1024 7.96
#    2048 8.01
# ...

