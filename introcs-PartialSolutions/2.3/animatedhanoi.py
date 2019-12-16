#-----------------------------------------------------------------------
# animatedhanoi.py
#-----------------------------------------------------------------------

import stdio
import stddraw
import stdarray
import sys

#-----------------------------------------------------------------------

# Draw the current state of the Towers of Hanoi game. pole[i] indicates
# the number of discs on pole i.

def draw(pole):

    POLE_WIDTH = 0.01
    POLE_COLOR = stddraw.RED
    DISC_COLOR = stddraw.BLUE

    n = len(pole) - 1

    # Draw 3 poles.
    stddraw.clear()
    stddraw.setPenColor(POLE_COLOR)
    stddraw.setPenRadius(POLE_WIDTH)
    for i in range(3):
        stddraw.line(i, 0, i, n)

    # Draw n discs.
    discs = stdarray.create1D(3, 0)   # discs[p] = # discs on pole p
    for i in range(n, 0, -1):
        stddraw.setPenColor(DISC_COLOR)
        stddraw.setPenRadius(0.035)   # magic constant
        size = 0.5 * i / n
        p = pole[i]
        stddraw.line(p-size/2, discs[p], p + size/2, discs[p])
        discs[p] += 1

    stddraw.show(500.0)

#-----------------------------------------------------------------------

def hanoiHelp(n, fromDisc, tempDisc, toDisc, pole):
    if n == 0:
        return
    hanoiHelp(n-1, fromDisc, toDisc, tempDisc, pole)
    stdio.writeln("Move disc " + str(n) + " from pole " + \
        str(fromDisc) + " to pole " + str(toDisc))
    pole[n] = toDisc
    draw(pole)
    hanoiHelp(n-1, tempDisc, fromDisc, toDisc, pole)

#-----------------------------------------------------------------------

def hanoi(n):
    # pole[i] = pole (0-2) that disc i is on.
    pole = stdarray.create1D(n+1, 0)
    draw(pole)
    hanoiHelp(n, 0, 1, 2, pole)

#-----------------------------------------------------------------------

# Accept integer command-line argument n. Solve the Towers of Hanoi
# problem with n discs. Write the sequence of moves to standard output.
# Animate to standard draw.

def main():
    
    WIDTH  = 200       # Width of largest disc
    HEIGHT = 15        # Height of each disc

    n = int(sys.argv[1])   # number of discs
    
    # Set size of window and sale
    stddraw.setCanvasSize(4*WIDTH, (n+3)*HEIGHT)
    stddraw.setXscale(-1, 3)
    stddraw.setYscale(0, n+3)

    # Solve the Towers of Hanoi with n discs
    hanoi(n)

    stddraw.show()

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python animatedhanoi.py 4
# Move disc 1 from pole 0 to pole 1
# Move disc 2 from pole 0 to pole 2
# Move disc 1 from pole 1 to pole 2
# Move disc 3 from pole 0 to pole 1
# Move disc 1 from pole 2 to pole 0
# Move disc 2 from pole 2 to pole 1
# Move disc 1 from pole 0 to pole 1
# Move disc 4 from pole 0 to pole 2
# Move disc 1 from pole 1 to pole 2
# Move disc 2 from pole 1 to pole 0
# Move disc 1 from pole 2 to pole 0
# Move disc 3 from pole 1 to pole 2
# Move disc 1 from pole 0 to pole 1
# Move disc 2 from pole 0 to pole 2
# Move disc 1 from pole 1 to pole 2

