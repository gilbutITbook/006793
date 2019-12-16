#-----------------------------------------------------------------------
# randomsurfer.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys
import random

# Accept an integer moves as a command-line argument. Read a
# transition matrix from standard input. Perform moves moves as
# prescribed by the transition matrix, and write to standard output
# the relative frequency of hitting each page.

moves = int(sys.argv[1])

n = stdio.readInt()
stdio.readInt() # Discard the second int of standard input.

# Read the transition matrix from standard input.
# p[i][j] is the probability that the surfer moves from
# page i to page j.
p = stdarray.create2D(n, n, 0.0)
for i in range(n):
    for j in range(n):
        p[i][j] = stdio.readFloat()

# Perform the simulation, thus computing the hits array.
# hits[i] is the number of times the surfer hits page i.
hits = stdarray.create1D(n, 0)
page = 0  # Start at page 0.
for i in range(moves):
    # Make one random move.
    r = random.random()
    total = 0.0
    for j in range(0, n):
        # Find interval containing r.
        total += p[page][j]
        if r < total:
            page = j
            break
    hits[page] += 1

# Write the page ranks.
for v in hits:
    stdio.writef("%8.5f", 1.0 * v / moves)
stdio.writeln()

#-----------------------------------------------------------------------

# python transition.py < tiny.txt | python randomsurfer.py 100
#  0.26000 0.27000 0.18000 0.26000 0.03000

# python transition.py < tiny.txt | python randomsurfer.py 10000
#  0.27410 0.26500 0.14570 0.24890 0.06630

# python transition.py < tiny.txt | python randomsurfer.py 10000000
#  0.27308 0.26568 0.14616 0.24719 0.06789
 
