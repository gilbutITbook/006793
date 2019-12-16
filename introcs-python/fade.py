#-----------------------------------------------------------------------
# fade.py
#-----------------------------------------------------------------------

import stddraw
import sys
from color import Color
from picture import Picture

#-----------------------------------------------------------------------

# Return a new Color object which blends Color objects c1 and c2 using
# alpha as the blending factor.

def blend(c1, c2, alpha):
    r = (1-alpha)*c1.getRed()   + alpha*c2.getRed()
    g = (1-alpha)*c1.getGreen() + alpha*c2.getGreen()
    b = (1-alpha)*c1.getBlue()  + alpha*c2.getBlue()
    return Color(int(r), int(g), int(b))

#-----------------------------------------------------------------------

# Accept strings sourceFile and targetFile and integer frameCount
# as command-line arguments. Read images from sourceFile and targetFile.
# Then, over the course of frameCount frames, gradually replace the
# image from sourceFile with the image with the image from targetFile.
# Display to standard draw each intermediate image. The images in the
# files can be in either JPG or PNG formats.

sourceFile = sys.argv[1]
targetFile = sys.argv[2]
n = int(sys.argv[3])       # number of intermediate frames

source = Picture(sourceFile)
target = Picture(targetFile)

width = source.width()
height = source.height()

stddraw.setCanvasSize(width, height)

pic = Picture(width, height)

for t in range(n+1):
    for col in range(width):
        for row in range(height):
            c0 = source.get(col, row)
            cn = target.get(col, row)
            alpha = float(t) / float(n)
            c = blend(c0, cn, alpha)
            pic.set(col, row, c)
    stddraw.picture(pic)
    stddraw.show(1000.0)

stddraw.show()


#-----------------------------------------------------------------------
    
# python fade.py mandrill.jpg darwin.jpg 7

# python fade.py mandrill.jpg darwin.jpg 5

# python fade.py mandrill.jpg darwin.png 7

# python fade.py mandrill.png darwin.jpg 7

# python fade.py mandrill.png darwin.png 7
