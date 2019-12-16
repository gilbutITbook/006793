#-----------------------------------------------------------------------
# estimatev.py
#-----------------------------------------------------------------------

import sys
import stdio
import percolationv
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
        if (percolationv.percolates(isOpen)):
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

# python estimatev.py 20 .75 10
# 0.0

# python estimatev.py 20 .95 10
# 1.0

# python estimatev.py 20 .85 10
# 0.3

# python estimatev.py 20 .85 1000
# 0.543

# python estimatev.py 20 .85 1000
# 0.56

# python estimatev.py 40 .85 100 
# 0.03
