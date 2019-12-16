#-----------------------------------------------------------------------
# selfavoid.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys
import random

# Accept integers n and trialCount as command-line arguments. Do
# trialCount random self-avoiding walks in an n-by-n lattice. 
# Write to standard output the percentage of dead ends encountered.

n      = int(sys.argv[1])
trials = int(sys.argv[2])
deadEnds = 0

for t in range(trials):

    # Create an n-by-n array, with all elements set to False.
    a = stdarray.create2D(n, n, False)

    x = n//2
    y = n//2
    while (x > 0) and (x < n-1) and (y > 0) and (y < n-1):
        # Check for dead end and make a random move.
        a[x][y] = True
        if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            deadEnds += 1
            break
        r = random.randrange(1, 5)
        if   (r == 1) and (not a[x+1][y]):
            x += 1
        elif (r == 2) and (not a[x-1][y]):
            x -= 1
        elif (r == 3) and (not a[x][y+1]):
            y += 1
        elif (r == 4) and (not a[x][y-1]):
            y -= 1

stdio.writeln(str(100*deadEnds//trials) + '% dead ends')

#-----------------------------------------------------------------------

# python selfavoid.py 5 100
# 0% dead ends

# python selfavoid.py 20 100
# 27% dead ends

# python selfavoid.py 40 100
# 80% dead ends

# python selfavoid.py 80 100
# 96% dead ends

# python selfavoid.py 5 1000
# 0% dead ends

# python selfavoid.py 20 1000
# 33% dead ends

# python selfavoid.py 40 1000
# 77% dead ends

# python selfavoid.py 80 1000
# 98% dead ends

