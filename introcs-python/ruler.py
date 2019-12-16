#-----------------------------------------------------------------------
# ruler.py
#-----------------------------------------------------------------------

import stdio

# Write to standard output the relative lengths of the subdivisions on
# a ruler. The nth line of output is the relative lengths of the marks
# on a ruler subdivided in intervals of 1/2^n of an inch.  For example,
# the fourth line of output gives the relative lengths of the marks
# that indicate intervals of one-sixteenth of an inch on a ruler.

ruler1 = '1'
ruler2 = ruler1 + ' 2 ' + ruler1
ruler3 = ruler2 + ' 3 ' + ruler2
ruler4 = ruler3 + ' 4 ' + ruler3
stdio.writeln(ruler1)
stdio.writeln(ruler2)
stdio.writeln(ruler3)
stdio.writeln(ruler4)

#-----------------------------------------------------------------------

# python ruler.py
# 1
# 1 2 1
# 1 2 1 3 1 2 1
# 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
