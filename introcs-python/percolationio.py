#-----------------------------------------------------------------------
# percolationio.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
import stdrandom

#-----------------------------------------------------------------------

# Return a random n-by-n matrix, each entry True with probability p.

def random(n, p):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    return a

#-----------------------------------------------------------------------

# Draw system a to standard draw. Parameter which indicates whether
# to display the entries corresponding to True or to False.

def draw(a, which):
    n = len(a)
    stddraw.setXscale(-.5, n)
    stddraw.setYscale(-.5, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, n-i-1, .5)

#-----------------------------------------------------------------------

# For testing.

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    test = random(n, p)
    draw(test, False)
    stddraw.show()
    
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python percolationio.py 10 0.8

