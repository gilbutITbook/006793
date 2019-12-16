#-----------------------------------------------------------------------
# binary.py
#-----------------------------------------------------------------------

import sys
import stdio

# Accept integer n as a command-line argument. Write the binary
# representation of n to standard output.

# Limitation: Does not handle negative integers.

n = int(sys.argv[1])

# Compute v as the largest power of 2 <= n.
v = 1
while v <= n//2:
    v *= 2

# Cast out powers of 2 in decreasing order.
while v > 0:
    if n < v:
        stdio.write(0)
    else:
        stdio.write(1)
        n -= v
    v //= 2

stdio.writeln()

#-----------------------------------------------------------------------

# python binary.py 19
# 10011

# python binary.py 255
# 11111111

# python binary.py 512
# 1000000000

# python binary.py 1000000000
# 111011100110101100101000000000
