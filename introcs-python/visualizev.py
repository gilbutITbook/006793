#-----------------------------------------------------------------------
# visualizev.py
#-----------------------------------------------------------------------

import sys
import stddraw
import percolationv
import percolationio

#-----------------------------------------------------------------------

# Accept integer n, float p, and integer t as command-line arguments.
# Generate a n-by-n random system with site vacancy probability p.
# Compute the directed percolation flow, and draw result to standard
# draw. Repeat t times.

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    for i in range(trials):
        isOpen = percolationio.random(n, p)
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        percolationio.draw(isOpen, False)
        stddraw.setPenColor(stddraw.BLUE)
        full = percolationv.flow(isOpen)
        percolationio.draw(full, True)
        stddraw.show(1000.0)
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python visualizev.py 20 .65 3

# python visualizev.py 20 .60 1

# python visualizev.py 20 .55 1

