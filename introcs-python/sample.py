#-----------------------------------------------------------------------
# sample.py
#-----------------------------------------------------------------------

import stdio
import sys
import stdarray
import random

# Accept integers m and n as command-line arguments. Write to standard
# output a random sample of m integers in the range 0...n-1 (no
# duplicates).

m = int(sys.argv[1]) # choose this many elements
n = int(sys.argv[2]) # from 0, 1, ..., n-1

# Initialize perm.
perm = stdarray.create1D(n, 0)
for i in range(n):
    perm[i] = i

# Create random sample in perm[0], perm[1], ..., perm[m-1]
for i in range(m):

    # Choose a random integer r between i and n-1.
    r = random.randrange(i, n)

    # Swap perm[i] and perm[r].
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp

# Write the results.
for i in range(m):
    stdio.write(str(perm[i]) + ' ')
stdio.writeln()

#-----------------------------------------------------------------------

# python sample.py 6 16      
# 9 6 3 5 4 13

# python sample.py 10 1000
# 566 240 662 680 500 491 309 348 563 34 

# python sample.py 20 20  
# 15 6 19 5 1 4 10 16 7 3 13 14 12 2 9 0 18 8 17 11 

