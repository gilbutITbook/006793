#-----------------------------------------------------------------------
# grayscale.py
#-----------------------------------------------------------------------

import sys
import stddraw
import luminance
from picture import Picture

#-----------------------------------------------------------------------

# Accept the name of a JPG or PNG file as a command-line argument.
# Read an image from the file with that name. Create and show a
# gray scale version of that image.

pic = Picture(sys.argv[1])

for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col, row)
        gray = luminance.toGray(pixel)
        pic.set(col, row, gray)

stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show()

#-----------------------------------------------------------------------

# python grayscale.py mandrill.jpg

# python grayscale mandrill.png

# python grayscale.py darwin.jpg

# python grayscale.py darwin.png

