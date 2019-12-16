#-----------------------------------------------------------------------
# ifs.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stdrandom
import stddraw

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Read a
# 1-by-m vector (probabilities) and two m-by-3 matrices (coefficients
# for updating x and y, respectively) from standard input. Plot the
# results as a set of n points to standard draw.

def main():
    n = int(sys.argv[1])
    dist = stdarray.readFloat1D()
    cx = stdarray.readFloat2D()
    cy = stdarray.readFloat2D()
    x = 0.0
    y = 0.0
    stddraw.setPenRadius(0.0)
    for i in range(n):
        r = stdrandom.discrete(dist)
        x0 = cx[r][0]*x + cx[r][1]*y + cx[r][2]
        y0 = cy[r][0]*x + cy[r][1]*y + cy[r][2]
        x = x0
        y = y0
        stddraw.point(x, y)
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python ifs.py 10000 < sierpinski.txt

# python ifs.py 10000 < barnsley.txt

# python ifs.py 10000 < binary.txt

# python ifs.py 10000 < coral.txt

# python ifs.py 10000 < culcita.txt

# python ifs.py 10000 < cyclosorus.txt

# python ifs.py 10000 < dragon.txt

# python ifs.py 10000 < fishbone.txt

# python ifs.py 10000 < floor.txt

# python ifs.py 10000 < koch.txt

# python ifs.py 10000 < spiral.txt

# python ifs.py 10000 < swirl.txt

# python ifs.py 10000 < tree.txt

# python ifs.py 10000 < zigzag.txt

