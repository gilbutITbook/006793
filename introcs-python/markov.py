#-----------------------------------------------------------------------
# markov.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys

# Accept integer moves from the command-line, and read a transition
# matrix from standard input. Compute the probabilities that a
# random surfer lands on each page (page ranks) after moves
# matrix-vector multiplies, and write the page ranks to standard
# output.

moves = int(sys.argv[1])

n = stdio.readInt()
stdio.readInt() # Discard the second int of standard input.

# Read the transition matrix from standard input.
# probs[i][j] is the probability that the surfer moves from
# page i to page j.
probs = stdarray.create2D(n, n, 0.0)
for i in range(n):
    for j in range(n):
        probs[i][j] = stdio.readFloat()

# Use the power method to compute page ranks.
ranks = stdarray.create1D(n, 0.0)
ranks[0] = 1.0
for i in range(moves):
    # Compute effect of next move on page ranks.
    newRanks = stdarray.create1D(n, 0.0)
    for j in range(n):
        # New rank of page j is dot product
        # of old ranks and column j of probs.
        for k in range(n):
            newRanks[j] += ranks[k] * probs[k][j]
    ranks = newRanks

# Write the page ranks.
for rank in ranks:
    stdio.writef("%8.5f", rank)
stdio.writeln()

#-----------------------------------------------------------------------

# python transition.py < tiny.txt | python3.4 markov.py 20
#  0.27245 0.26515 0.14669 0.24764 0.06806

# python transition.py < tiny.txt | python3.4 markov.py 40
#  0.27303 0.26573 0.14618 0.24723 0.06783

