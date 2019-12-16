#-----------------------------------------------------------------------
# merge.py
#-----------------------------------------------------------------------

import sys
import stdio
import stdarray

#-----------------------------------------------------------------------

# Merge a[lo:mid] with a[mid:hi] using aux as auxiliary memory.

def _merge(a, lo, mid, hi, aux):
    n = hi - lo
    i = lo
    j = mid
    for k in range(n):
        if i == mid:
            aux[k] = a[j]
            j += 1
        elif j == hi:
            aux[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]
            j += 1
        else:
            aux[k] = a[i]
            i += 1
    a[lo:hi] = aux[0:n]

#-----------------------------------------------------------------------

# Sort a[lo:hi] into increasing order, using array aux as auxiliary
# memory.

def _sort(a, lo, hi, aux):
    n = hi - lo
    if n <= 1:
        return
    mid = (lo + hi) // 2
    _sort(a, lo, mid, aux)
    _sort(a, mid, hi, aux)
    _merge(a, lo, mid, hi, aux)

#-----------------------------------------------------------------------

# Sort array a into increasing order.

def sort(a):
    n = len(a)
    aux = stdarray.create1D(n)
    _sort(a, 0, n, aux)

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

#-----------------------------------------------------------------------

# more tiny.txt 
# the and was his you tom but for had him 

# python merge.py < tiny.txt
# and but for had him his the tom was you 

# python insertion.py < tomsawyer.txt
# ... (Works quickly.)

