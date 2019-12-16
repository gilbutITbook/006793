#-----------------------------------------------------------------------
# couponcollector.py
#-----------------------------------------------------------------------

import stdio
import sys
import stdarray
import random

# Accept integer n as a command-line argument. Write to standard
# output the number of coupons you collect before obtaining one of
# each of n types.

n = int(sys.argv[1])

count = 0
collectedCount = 0
isCollected = stdarray.create1D(n, False)

while collectedCount < n:
    # Generate another coupon.
    value = random.randrange(0, n)
    count += 1
    if not isCollected[value]:
        collectedCount += 1
        isCollected[value] = True

stdio.writeln(count)

#-----------------------------------------------------------------------

# python couponcollector.py 1000
# 8507

# python couponcollector.py 1000
# 6602

# python couponcollector.py 1000000
# 14238292
