#-----------------------------------------------------------------------
# insertion.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Exchange a[i] and a[j].

def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]

#-----------------------------------------------------------------------

# Sort array a into increasing order.

def sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while (j > 0) and (a[j] < a[j-1]):
            exchange(a, j-1, j)
            j -= 1

#-----------------------------------------------------------------------

# Read strings from standard input, sort them into
# increasing order, and write them to standard output.

def main():
    a = stdio.readAllStrings()
    sort(a)
    for s in a:
        stdio.write(s + ' ')
    stdio.writeln()

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

# more tiny.txt 
# the and was his you tom but for had him

# python insertion.py < tiny.txt 
# and but for had him his the tom was you 

# python insertion.py < tomsawyer.txt
# ... (Works, but takes a very long time.)

