#-----------------------------------------------------------------------
# randomseq.py
#-----------------------------------------------------------------------

import stdio
import sys
import random

# Accept integer command-line argument n. Write to standard output
# a random sequence of n floats in the range [0, 1).

n = int(sys.argv[1])
for i in range(n):
    stdio.writeln(random.random())
    
#-----------------------------------------------------------------------

# python randomseq.py 10
# 0.3047021850662529
# 0.2315506953328379
# 0.4735912595440809
# 0.4865769720408386
# 0.4982226515715956
# 0.1613938366431179
# 0.5621482228061883
# 0.6852024702215561
# 0.9833084725966769
# 0.7462654982265501
