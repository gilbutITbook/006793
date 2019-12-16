#-----------------------------------------------------------------------
# rangefilter.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer command-line arguments lo and hi. Read integers from
# standard input until end-of-file. Write to standard output each of
# those integers that is in the range lo to hi, inclusive.

lo = int(sys.argv[1])
hi = int(sys.argv[2])
while not stdio.isEmpty():
    # Process one integer.
    value = stdio.readInt()
    if (value >= lo) and (value <= hi):
        stdio.write(str(value) + ' ')
stdio.writeln()

#-----------------------------------------------------------------------

# python rangefilter.py 100 400
# 358 1330 55 165 689 1014 3066 387 575 843 203 48 292 877 65 998
# 358 165 387 203 292

