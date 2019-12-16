#-----------------------------------------------------------------------
# timesort.py
#-----------------------------------------------------------------------

import stdio
import stdrandom
import stdarray
from stopwatch import Stopwatch

#-----------------------------------------------------------------------

# Run function f for arrays of n random floats, performing the
# experiment trials times. Return the amount of wall-clock time
# consumed.

def timeTrials(f, n, trials):
    total = 0.0
    a = stdarray.create1D(n, 0.0)
    for t in range(trials):
        for i in range(n):
            a[i] = stdrandom.uniformFloat(0.0, 1.0)
        watch = Stopwatch()
        f(a)
        total += watch.elapsedTime()
    return total
    
#-----------------------------------------------------------------------

# Perform a doubling test of the performance of function f starting
# at n, doubling n, and writing the ration of the time for the
# current n and the time for the previous n each time through the
# loop. Perform trials trials for each n.

def doublingTest(f, n, trials):
    while True:
        prev = timeTrials(f, n // 2, trials)
        curr = timeTrials(f, n,      trials)
        ratio = curr / prev
        stdio.writef('%7d %4.2f\n', n, ratio)
        n *= 2

#-----------------------------------------------------------------------

# python
# Python 3.4.3 (default, May 25 2015, 18:48:21) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import insertion
# >>> import timesort
# >>> timesort.doublingTest(insertion.sort, 128, 100)
#     128 3.67
#     256 3.73
#     512 4.21
#    1024 4.19
#    2048 4.11


# python
# Python 3.4.3 (default, May 25 2015, 18:48:21) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import merge
# >>> import timesort
# >>> timesort.doublingTest(merge.sort, 128, 100)
#     128 1.84
#     256 2.15
#     512 2.22
#    1024 2.17
#    2048 2.13
#    4096 2.12
#    8192 2.14

