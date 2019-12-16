#-----------------------------------------------------------------------
# bigarray.py
#-----------------------------------------------------------------------

import sys
import stdio
import stdarray

n = int(sys.argv[1])
a = stdarray.create1D(n, 0)
stdio.writeln('finished')

#-----------------------------------------------------------------------

# python bigarray.py 100000000
# finished

# python bigarray.py 1000000000
# finished

# python bigarray.py 10000000000
# Killed: 9

