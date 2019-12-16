#-----------------------------------------------------------------------
# towersofhanoi.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Write to standard output instructions to move n Towers of Hanoi
# disks to the left (if parameter left is True) or to the right (if
# parameter left is False).

def moves(n, left):
    if n == 0:
        return
    moves(n-1, not left)
    if left:
        stdio.writeln(str(n) + ' left')
    else:
        stdio.writeln(str(n) + ' right')
    moves(n-1, not left)

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard output
# instructions to move n Towers of Hanoi disks to the left.

def main():
    n = int(sys.argv[1])
    moves(n, True)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python towersofhanoi.py 1
# 1 left

# python towersofhanoi.py 2
# 1 right
# 2 left
# 1 right

# python towersofhanoi.py 3
# 1 left
# 2 right
# 1 left
# 3 left
# 1 left
# 2 right
# 1 left

# python towersofhanoi.py 4
# 1 right
# 2 left
# 1 right
# 3 right
# 1 right
# 2 left
# 1 right
# 4 left
# 1 right
# 2 left
# 1 right
# 3 right
# 1 right
# 2 left
# 1 right

