#-----------------------------------------------------------------------
# divisorpattern.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer command-line argument n. Write to standard output
# an n-by-n table with an asterisk in row i and column j if either
# i divides j or j divides i.

n = int(sys.argv[1])

for i in range(1, n+1):
    # Write the ith line.
    for j in range(1, n+1):
        # Write the jth entry in the ith line.
        if (i % j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write('  ')
    stdio.writeln(i)

#-----------------------------------------------------------------------

# python divisorpattern.py 0

# python divisorpattern.py 1
# * 1

# python divisorpattern.py 2
# * * 1
# * * 2

# python divisorpattern.py 3
# * * * 1
# * *   2
# *   * 3

# python divisorpattern.py 4
# * * * * 1
# * *   * 2
# *   *   3
# * *   * 4

# python divisorpattern.py 5
# * * * * * 1
# * *   *   2
# *   *     3
# * *   *   4
# *       * 5

