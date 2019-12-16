#-----------------------------------------------------------------------
# htree.py
#-----------------------------------------------------------------------

import stddraw
import sys

#-----------------------------------------------------------------------

# Draw to standard draw a level n H-tree centered at (x. y) with lines
# of length lineLength.

def draw(n, lineLength, x, y):
    if n == 0:
        return
    x0 = x - lineLength/2
    x1 = x + lineLength/2
    y0 = y - lineLength/2
    y1 = y + lineLength/2

    stddraw.line(x0, y, x1, y)
    stddraw.line(x0, y0, x0, y1)
    stddraw.line(x1, y0, x1, y1)

    draw(n-1, lineLength/2, x0, y0)
    draw(n-1, lineLength/2, x0, y1)
    draw(n-1, lineLength/2, x1, y0)
    draw(n-1, lineLength/2, x1, y1)

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Draw a level n H-tree
# centered at (.5, .5) with lines of length .5.

def main():
    n = int(sys.argv[1])
    stddraw.setPenRadius(0.0)
    draw(n, .5, .5, .5)
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python htree.py 3

# python htree.py 4

# python htree.py 5
