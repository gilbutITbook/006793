#-----------------------------------------------------------------------
# wordcount.py
#-----------------------------------------------------------------------

import stdio

# Read a sequence of strings from standard input, and write the number
# of strings to standard output.

count = 0

while not stdio.isEmpty():
    word = stdio.readString()
    count += 1

stdio.writeln('number of words  = ' + str(count))

#-----------------------------------------------------------------------

# python wordcount.py < tale.txt 
# number of words  = 139043

