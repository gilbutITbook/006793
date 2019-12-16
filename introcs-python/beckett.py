#-----------------------------------------------------------------------
# beckett.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Write to standard output Beckett's stage instructions to have n
# actors enter (if parameter enter is True) or exit (if parameter
# enter is False) the stage.

def moves(n, enter):
    if n == 0:
        return
    moves(n-1, True)
    if enter:
        stdio.writeln('enter ' + str(n))
    else:
        stdio.writeln('exit  ' + str(n))
    moves(n-1, False)

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard
# output Beckett's stage instructions (the bit positions that change
# in a binary-reflected Gray code) for n actors.

def main():
    n = int(sys.argv[1])
    moves(n, True)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python beckett.py 1
# enter 1

# python beckett.py 2
# enter 1
# enter 2
# exit  1

# python beckett.py 3
# enter 1
# enter 2
# exit  1
# enter 3
# enter 1
# exit  2
# exit  1

# python beckett.py 4
# enter 1
# enter 2
# exit  1
# enter 3
# enter 1
# exit  2
# exit  1
# enter 4
# enter 1
# enter 2
# exit  1
# exit  3
# enter 1
# exit  2
# exit  1

