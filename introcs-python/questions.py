#-----------------------------------------------------------------------
# questions.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Return the hidden integer in the range [lo, hi) by writing
# "Greater than or equal to" questions to standard output and
# reading True/False replies from standard input.

def search(lo, hi):
    if (hi - lo) == 1:
        return lo
    mid = (hi + lo) // 2
    stdio.write('Greater than or equal to ' + str(mid) + '?  ')
    if stdio.readBool():
        return search(mid, hi)
    else:
        return search(lo, mid)

#-----------------------------------------------------------------------

# Accept integer command-line argument k. Ask the user to think of
# an integer between 0 and (2**k)-1. Write "Greater than or equal to?"
# questions to standard output, in binary search fashion. Read
# True/False replies from standard input. Write the integer to
# standard output.

k = int(sys.argv[1])
n = 2 ** k
stdio.write('Think of a number ')
stdio.writeln('between 0 and ' + str(n-1))
guess = search(0, n)
stdio.writeln('Your number is ' + str(guess))

#-----------------------------------------------------------------------

# python questions.py 7
# Think of a number between 0 and 127
# Greater than or equal to 64?  True
# Greater than or equal to 96?  False
# Greater than or equal to 80?  False
# Greater than or equal to 72?  True
# Greater than or equal to 76?  True
# Greater than or equal to 78?  False
# Greater than or equal to 77?  True
# Your number is 77

