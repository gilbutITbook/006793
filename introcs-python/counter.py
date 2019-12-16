#-----------------------------------------------------------------------
# counter.py
#-----------------------------------------------------------------------

import sys
import stdio
#import stdarray
import stdrandom

class Counter:

    def __init__(self, id, maxCount):
        self._name = id            # Counter name
        self._maxCount = maxCount  # Maximum value
        self._count = 0            # Value

    def increment(self):
        if self._count < self._maxCount:
            self._count += 1

    def value(self):
        return self._count

    def __str__(self):
        return self._name + ': ' + str(self._count)

    def __eq__(self, other):
        return self._count == other._count

    def __ne__(self, other):
        return self._count != other._count

    def __lt__(self, other):
        return self._count < other._count

    def __gt__(self, other):
        return self._count > other._count

    def __le__(self, other):
        return self._count <= other._count

    def __ge__(self, other):
        return self._count >= other._count

#-----------------------------------------------------------------------

# For testing.
# Accept integer command-line argument n and float command-line
# argument p. Flip a coin (whose heads probability is p) n times.
# Write to standard output the number of heads and tails.

def main():

    n = int(sys.argv[1])
    p = float(sys.argv[2])
    
    heads = Counter('Heads', n)
    tails = Counter('Tails', n)
    
    for i in range(n):
        if stdrandom.bernoulli(p):
            heads.increment()
        else:
            tails.increment()
    
    stdio.writeln(heads)
    stdio.writeln(tails)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python counter.py 1000 .5
# Heads: 483
# Tails: 517

# python counter.py 1000 .5
# Heads: 503
# Tails: 497

# python counter.py 1000 .3
# Heads: 280
# Tails: 720

