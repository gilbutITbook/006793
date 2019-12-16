#-----------------------------------------------------------------------
# percolationv.py
#-----------------------------------------------------------------------

import stdarray
import stdio

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system. 
# Compute and return a matrix that represents the full sites of
# that system. For now, consider only vertical percolation.

def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n, n, False)
    for j in range(n):
        isFull[0][j] = isOpen[0][j]
    for i in range(1, n):
        for j in range(n):
            if isOpen[i][j] and isFull[i-1][j]:
                isFull[i][j] = True
    return isFull

#-----------------------------------------------------------------------

# open is matrix that represents the open sites of a system. Return
# True if that system percolates, and False otherwise.

def percolates(isOpen):
    
    # Compute the full sites of the system.
    isFull = flow(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull)
    for j in range(n):
        if isFull[n-1][j]:
            return True
    return False

#-----------------------------------------------------------------------

# Read from standard input a boolean matrix that represents the
# open sites of a system. Write to standard output a boolean
# matrix representing the full sites of the system. Then write
# True if the system percolates and False otherwise.

def main():
    isOpen = stdarray.readBool2D()
    stdarray.write2D(flow(isOpen))
    stdio.writeln(percolates(isOpen))
    
if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python percolationv.py < test5.txt
# 5 5
# 0 1 1 0 1 
# 0 0 1 0 1 
# 0 0 0 0 1 
# 0 0 0 0 1 
# 0 0 0 0 1 
# True

# python percolationv.py < test8.txt
# 8 8
# 0 0 1 1 1 0 0 0 
# 0 0 0 1 1 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# False

