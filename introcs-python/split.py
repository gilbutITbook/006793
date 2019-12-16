#-----------------------------------------------------------------------
# split.py
#-----------------------------------------------------------------------

import sys
import stdarray
from instream import InStream
from outstream import OutStream

#-----------------------------------------------------------------------

# Accept string fileName and integer fieldCount as command-line
# arguments. Split the file whose name is fileName.csv, by field,
# into fieldCount+1 files named fileName1.txt, fileName2.txt, etc.

DELIM = ','

fileName = sys.argv[1]
fieldCount = int(sys.argv[2])

# Create the input stream.
inStream = InStream(fileName + '.csv')

# Create output streams.
outStreams = stdarray.create1D(fieldCount)
for i in range(fieldCount):
    file = OutStream(fileName + str(i) + '.txt')
    outStreams[i] = file

# Read lines from the input stream and write them to the
# output stream.
while inStream.hasNextLine():
    line = inStream.readLine()
    fields = line.split(DELIM)
    for i in range(fieldCount):
        outStreams[i].writeln(fields[i])

#-----------------------------------------------------------------------

# more djia.csv
# Date,Open,High,Low,Close,Volume,Adj. Close*
# 17-Mar-06,11294.94,11294.94,11253.23,11279.65,2549619968,11279.65
# 16-Mar-06,11210.97,11324.80,11176.07,11253.24,2292179968,11253.24
# 15-Mar-06,11149.76,11258.28,11097.23,11209.77,2292999936,11209.77
# ...

# python split.py djia 3

# more djia0.txt
# Date
# 17-Mar-06
# 16-Mar-06
# 15-Mar-06
# ...

# more djia1.txt
# Open
# 11294.94
# 11210.97
# 11149.76
# ...

# more djia2.txt
# High
# 11294.94
# 11324.80
# 11258.28
# ...

# more djia3.txt
# Low
# 11253.23
# 11176.07
# 11097.23
# ...

