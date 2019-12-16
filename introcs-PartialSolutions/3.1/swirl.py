#-----------------------------------------------------------------------
# swirl.py
#-----------------------------------------------------------------------

import sys
import math
import stddraw
from picture import Picture

# Accept a file name as a command-line argument. Read the image from
# the specified file, swirl the image, and display the original image
# and the swirled image.

pic1 = Picture(sys.argv[1])

width  = pic1.width()
height = pic1.height()

col0 = 0.5 * (float(width)  - 1.0)
row0 = 0.5 * (float(height) - 1.0)

pic2 = Picture(width, height)

# Compute the swirl.
for sCol in range(width):
    for sRow in range(height):
        dCol = float(sCol) - col0
        dRow = float(sRow) - row0
        r = math.sqrt(dCol*dCol + dRow*dRow)
        angle = math.pi / 256.0 * r
        tCol = int(dCol * math.cos(angle) - dRow * math.sin(angle) + col0)
        tRow = int(dCol * math.sin(angle) + dRow * math.cos(angle) + row0)

        # Plot pixel (sx, sy) the same color as (tx, ty) if it's
        # in bounds
        if (tCol >= 0) and (tCol < width) and \
           (tRow >= 0) and (tRow < height):
            pic2.set(sCol, sRow, pic1.get(tCol, tRow))

stddraw.setCanvasSize(width, height);
stddraw.picture(pic2)
stddraw.show()

#-----------------------------------------------------------------------

# python swirl.py mandrill.jpg

# python swirl.py mandrill.png

# python swirl.py darwin.jpg

# python swirl.py darwin.png
