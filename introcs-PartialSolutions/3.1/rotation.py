#-----------------------------------------------------------------------
# rotation.py
#-----------------------------------------------------------------------

import sys
import math
import stddraw
from picture import Picture

# Accept an image file and a number of degrees as commmand-line
# arguments. Rotate the image by the specified number of degrees.
# Display the original image and the rotated one.

pic1 = Picture(sys.argv[1])

width  = pic1.width()
height = pic1.height()

angle = math.radians(float(sys.argv[2]))
sin = math.sin(angle)
cos = math.cos(angle)
x0 = 0.5 * (float(width)  - 1.0)     # point to rotate about
y0 = 0.5 * (float(height) - 1.0)     # center of image

pic2 = Picture(width, height)

# Perform the rotation.
for col in range(width):
    for row in range(height):
        a = float(col) - x0
        b = float(row) - y0
        cc = int(a * cos - b * sin + x0)
        rr = int(a * sin + b * cos + y0)

        # Plot pixel (col, row) the same color as (cc, rr) if it's
        # in bounds.
        if (cc >= 0) and (cc < width) and \
           (rr >= 0) and (rr < height):
            pic2.set(col, row, pic1.get(cc, rr))

stddraw.setCanvasSize(width, height)
stddraw.picture(pic2)
stddraw.show()
    
#-----------------------------------------------------------------------

# python rotation.py mandrill.jpg 30

# python rotation.py mandrill.jpg 45

# python rotation.py mandrill.png 30

# python rotation.py darwin.jpg 30

# python rotation.py darwin.png 30
