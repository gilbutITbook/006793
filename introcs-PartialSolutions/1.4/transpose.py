#-----------------------------------------------------------------------
# transpose.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer command-line argument n. Create an n-by-n array and
# write it to standard output. Then transpose it in-place and write
# the result to standard output.

# Original Java version by Christian Rubio.

# Create an n-by-n array of zeros.
n = int(sys.argv[1])
a = stdarray.create2D(n, n, 0)

# Write the initial array.
stdio.writeln("Before");
stdio.writeln("------");
for row in a:
    for element in row:
        stdio.write(str(element) + '  ')
    stdio.writeln()

# Transpose the array in-place.
for r in range(n):
    for c in range(r+1, n):
        temp = a[r][c]
        a[r][c] = a[c][r]
        a[c][r] = temp

# Write the transposed array.
stdio.writeln()
stdio.writeln("After")
stdio.writeln("------")
for row in a:
    for element in row:
        stdio.write(str(element) + '  ')
    stdio.writeln()
    
#-----------------------------------------------------------------------

# python transpose.py 0
# Before
# ------
# 
# After
# ------

# python transpose.py 1
# Before
# ------
# 0  
# 
# After
# ------
# 0  

# python transpose.py 2
# Before
# ------
# 0  1  
# 2  3  
# 
# After
# ------
# 0  2  
# 1  3  
# 

# python transpose.py 5
# Before
# ------
# 0  1  2  3  4  
# 5  6  7  8  9  
# 10  11  12  13  14  
# 15  16  17  18  19  
# 20  21  22  23  24  
# 
# After
# ------
# 0  5  10  15  20  
# 1  6  11  16  21  
# 2  7  12  17  22  
# 3  8  13  18  23  
# 4  9  14  19  24  

