#-----------------------------------------------------------------------
# cat.py
#-----------------------------------------------------------------------

import sys
from instream import InStream
from outstream import OutStream

# Copy files or web pages whose names are given by sys.argv[1:n-2]
# to the file whose name is given by sys.argv[n-1].

inFilenames = sys.argv[1:len(sys.argv)-1]
outFilename = sys.argv[len(sys.argv)-1]
outstream = OutStream(outFilename)
for filename in inFilenames:
    instream = InStream(filename)
    s = instream.readAll()
    outstream.write(s)

#-----------------------------------------------------------------------

# more in1.txt
# This is

# more in2.txt
# a tiny
# test.

# python cat.py in1.txt in2.txt out.txt

# more out.txt
# This is
# a tiny
# test.

