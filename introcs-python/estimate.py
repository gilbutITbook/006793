#-----------------------------------------------------------------------
# estimate.py
#-----------------------------------------------------------------------

import sys
import stdio
import percolation
import percolationio

#-----------------------------------------------------------------------

# Generate a random n-by-n system with site vacancy probability p
# and determine if the system percolates. Repeat t times. Return
# an estimate of the empirical percolation probability of such systems.

def evaluate(n, p, trials):
    count = 0
    for i in range(trials):
        # Generate one random network.
        isOpen = percolationio.random(n, p)
        if (percolation.percolates(isOpen)):
            count += 1
    return 1.0 * count / trials

#-----------------------------------------------------------------------

# Accept integer n, float p, and integer trials as command-line
# arguments. Create trials random n-by-n systems with site vacancy
# probability p. Determine the fraction of them that percolate, and
# write that fraction to standard output.

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    q = evaluate(n, p, trials)
    stdio.writeln(q)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python2.7 estimate.py 20 .55 100
# 0.25

# python2.7 estimate.py 20 .65 100
# 0.88

# python2.7 estimate.py 20 .65 100
# 0.89

# python2.7 estimate.py 40 .55 1000
# 0.094

