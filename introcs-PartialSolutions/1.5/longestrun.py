#-----------------------------------------------------------------------
# longestrun.py
#-----------------------------------------------------------------------

import stdio
import sys

# Read a sequence of integers from standard input, and write to 
# standard output the integer that appears in a longest consecutive
# run. Also write the length of the run.

# Handle the degenerate case with no input integers.
if stdio.isEmpty():
    stdio.writeln('no longest consecutive run')
    sys.exit()

prev = stdio.readInt();
count = 1
best      = prev
bestCount = count

while not stdio.isEmpty():
    # Read the next value.
    current = stdio.readInt()

    # Update the current run.
    if current == prev:
        count += 1
    else:
        prev = current
        count = 1

    # Update champion values
    if count > bestCount:
        bestCount = count
        best      = current
      
# Write the results.
stdio.writeln('Longest run: ' + str(bestCount) + \
              ' consecutive ' + str(best) + 's')

#-----------------------------------------------------------------------

# python longestrun.py
# 1 2 2 1 5 1 1 7 7 7 7 1 1 
# Longest run: 4 consecutive 7s

