#-----------------------------------------------------------------------
# inversepermutation.py
#-----------------------------------------------------------------------

import stdio
import sys
import stdarray

# Accept a permutation of integers from the command line and write the
# inverse permutation to standard output.

# Accept the permutation.
perm = []
for i in range(1, len(sys.argv)):
    perm += [int(sys.argv[i])]
n = len(perm)

# Make sure the permutation is valid.
exists = stdarray.create1D(n, False)
for i in range(n):
    if (perm[i] < 0) or (perm[i] >= n) or exists[perm[i]]:
        stdio.writeln("Not a permutation")
        sys.exit(0)
    exists[perm[i]] = True

# Invert the permutation.
permInverted = [0] * n
for i in range(n):
    permInverted[perm[i]] = i

# Write the inverted permutation.
for element in permInverted:
    stdio.write(str(element) + ' ')
stdio.writeln()

#-----------------------------------------------------------------------


# python inversepermutation.py 0 1 2 3 4 5
# 0 1 2 3 4 5 

# python inversepermutation.py 5 4 3 2 1 0
# 5 4 3 2 1 0 

# python inversepermutation.py 5 3 4 0 1 2
# 3 4 5 1 2 0

# python inversepermutation.py 1 2 3 4 5
# Not a permutation

