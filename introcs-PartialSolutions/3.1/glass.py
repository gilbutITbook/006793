#-----------------------------------------------------------------------
# glass.py
#-----------------------------------------------------------------------

import sys
import random
import stddraw
import stdrandom
from picture import Picture

# Accept a command-line argument argument which is a file name. Read
# an image from that file. Apply an image filter that makes it look
# like the image is being seen through glass. This effect is
# accomplished by plotting each pixel the color of a random
# neighboring pixel. Display the original image and the new one.

pic1 = Picture(sys.argv[1])

width  = pic1.width()
height = pic1.height()

pic2 = Picture(width, height)

for col in range(width):
    for row in range(height):
        cc = (width  + col + stdrandom.uniformInt(-5, 6)) % width
        rr = (height + row + stdrandom.uniformInt(-5, 6)) % height
        c = pic1.get(cc, rr)
        pic2.set(col, row, c)

stddraw.setCanvasSize(width, height)
stddraw.picture(pic2)
stddraw.show()

#-----------------------------------------------------------------------

# python glass.py mandrill.jpg

# python glass.py mandrill.png

# python glass.py darwin.jpg

# python glass.py darwin.png

