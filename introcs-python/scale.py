#-----------------------------------------------------------------------
# scale.py
#-----------------------------------------------------------------------

import stddraw
import sys
from picture import Picture

#-----------------------------------------------------------------------

# Accept the name of a JPG or PNG image file, an integer w, and
# an integer h as command line arguments. Read an image from the
# file, and display the image scaled to width w and height h.

fileName = sys.argv[1]
w = int(sys.argv[2])
h = int(sys.argv[3])

source = Picture(fileName)
target = Picture(w, h)

for tCol in range(w):
    for tRow in range(h):
        sCol = tCol * source.width() // w
        sRow = tRow * source.height() // h
        target.set(tCol, tRow, source.get(sCol, sRow))

stddraw.setCanvasSize(w, h)
stddraw.picture(target)
stddraw.show()

#-----------------------------------------------------------------------

# python scale.py mandrill.jpg 800 800

# python scale.py mandrill.jpg 600 300

# python scale.py mandrill.jpg 200 400

# python scale.py mandrill.jpg 200 200

# python scale.py mandrill.png 200 200

# python scale.py darwin.jpg 200 200

# python scale.py darwin.png 200 200

