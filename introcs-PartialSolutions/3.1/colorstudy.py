#-----------------------------------------------------------------------
# colorstudy.py
#-----------------------------------------------------------------------

import stddraw
from color import Color

# Display Albers squares corresponding to each of 256 levels
# of blue (blue-to-white in row-major order) and gray
# (black-to-white in column-major order).

stddraw.setXscale(-1, 16)
stddraw.setYscale(-1, 16)

for i in range(16):
    for j in range(16):     
        c = Color((15-j)*255/15, (15-j)*255/15, 255)            
        stddraw.setPenColor(c)
        stddraw.filledSquare(i, j, 0.5)
        #stddraw.show(0.0)
        
for i in range(16):
    for j in range(16):     
        c = Color(i*255/15, i*255/15, i*255/15)
        stddraw.setPenColor(c)
        stddraw.filledSquare(i, j, 0.25)
        #stddraw.show(0.0)        
        
stddraw.show()

#-----------------------------------------------------------------------

# python colorstudy.py

