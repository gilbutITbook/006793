#-----------------------------------------------------------------------
# coupon.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys
import random

#-----------------------------------------------------------------------

# Return a random coupon between 0 and n-1.

def getCoupon(n):
    return random.randrange(0, n)

#-----------------------------------------------------------------------

# Collect coupons until getting one of each value in the range
# 0 to n-1.  Return the number of coupons collected.

def collect(n):
    found = stdarray.create1D(n, False)
    couponCount = 0
    distinctCouponCount = 0
    while distinctCouponCount < n:
        coupon = getCoupon(n)
        couponCount += 1
        if not found[coupon]:
            distinctCouponCount += 1
            found[coupon] = True
    return couponCount

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard
# output the number of coupons you collect before obtaining one of
# each of n types.

n = int(sys.argv[1])
couponCount = collect(n)
stdio.writeln(couponCount)

#-----------------------------------------------------------------------

# python coupon.py 1000
# 6456

# python coupon.py 1000
# 8815

# python coupon.py 1000000
# 16079795

