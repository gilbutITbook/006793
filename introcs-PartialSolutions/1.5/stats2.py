#-----------------------------------------------------------------------
# stats2.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# Accept integer command-line argument n. Then read n floats from
# standard input, and write their mean and standard deviation to
# standard output.

n = int(sys.argv[1])

# Read the floats.
a = []
for i in range(n):
    a += [stdio.readFloat()]

# Compute the mean.
total = 0.0
for element in a:
    total += element
mean = total / float(n)

# Compute the standard deviation.
total2 = 0.0
for element in a:
    total2 += (element - mean) ** 2
stddev = math.sqrt(total2) / float(n - 1)

# Write the results.
stdio.writeln('Mean               = ' + str(mean))
stdio.writeln('Standard deviation = ' + str(stddev))

#-----------------------------------------------------------------------

# python stats2.py 10
# 4 5 8 7 2 0 9 4 3 2
# Mean               = 4.4
# Standard deviation = 0.9583937179043479

