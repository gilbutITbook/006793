#-----------------------------------------------------------------------
# hadamard.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys

# Accept integer command-line argument n. Write to standard output
# the Hadamard matrix of order n. Assume that n is a power of 2.

n = int(sys.argv[1])

# Create the matrix.
H = stdarray.create2D(n, n, True)

# Initialize Hadamard matrix of order n.
i1 = 1
while i1 < n:
    for i2 in range(i1):
        for i3 in range(i1):
            H[i2+i1][i3]    = H[i2][i3]
            H[i2][i3+i1]    = H[i2][i3]
            H[i2+i1][i3+i1] = not H[i2][i3]
    i1 += i1

# Write the matrix.
for i in range(n):
    for j in range(n):
        if H[i][j]:
            stdio.write('T ')
        else:
            stdio.write('F ')
    stdio.writeln()
    
#-----------------------------------------------------------------------

# python hadamard.py 2
# T T 
# T F 

# python hadamard.py 4
# T T T T 
# T F T F 
# T T F F 
# T F F T 

# python hadamard.py 8
# T T T T T T T T 
# T F T F T F T F 
# T T F F T T F F 
# T F F T T F F T 
# T T T T F F F F 
# T F T F F T F T 
# T T F F F F T T 
# T F F T F T T F 

# python hadamard.py 16
# T T T T T T T T T T T T T T T T 
# T F T F T F T F T F T F T F T F 
# T T F F T T F F T T F F T T F F 
# T F F T T F F T T F F T T F F T 
# T T T T F F F F T T T T F F F F 
# T F T F F T F T T F T F F T F T 
# T T F F F F T T T T F F F F T T 
# T F F T F T T F T F F T F T T F 
# T T T T T T T T F F F F F F F F 
# T F T F T F T F F T F T F T F T 
# T T F F T T F F F F T T F F T T 
# T F F T T F F T F T T F F T T F 
# T T T T F F F F F F F F T T T T 
# T F T F F T F T F T F T T F T F 
# T T F F F F T T F F T T T T F F 
# T F F T F T T F F T T F T F F T 

