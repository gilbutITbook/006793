#-----------------------------------------------------------------------
# factors.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.

n = int(sys.argv[1])

factor = 2
while factor*factor <= n:
    while n % factor == 0:
        # Cast out and write factor.
        n //= factor
        stdio.write(str(factor) + ' ')
    factor += 1
    # Any factors of n are greater than or equal to factor.

if n > 1:
    stdio.write(n)
stdio.writeln()

#-----------------------------------------------------------------------

# python factors.py 3757208    
# 2 2 2 7 13 13 397

# python factors.py 287994837222311
# 17 1739347 9739789
