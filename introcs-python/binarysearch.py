#-----------------------------------------------------------------------
# binarysearch.py
#-----------------------------------------------------------------------

import sys
import stdio
import instream

#-----------------------------------------------------------------------

# Return the index of key in array a[lo:hi], or -1 if key is not
# present.

def _search(key, a, lo, hi):
    if hi <= lo:
        return -1
    mid = (lo + hi) // 2

    # Python 2.6 implements a cmp() function which calls a __cmp__()
    # method.  But Python 3.x does not.  So must use < instead.

    if key < a[mid]:
        return _search(key, a, lo, mid)
    elif a[mid] < key:
        return _search(key, a, mid+1, hi)
    else:
        return mid

#-----------------------------------------------------------------------

# Return the index of key in array a, or -1 if key is not present.

def search(key, a):
    return _search(key, a, 0, len(a))

#-----------------------------------------------------------------------

# Accept as a command-line argument a string which is the name of a
# whitelist file. Write to standard output the keys in standard input
# that are not in the whitelist file.

def main():
    inStream = instream.InStream(sys.argv[1])
    a = inStream.readAllStrings()

    while not stdio.isEmpty():
        key = stdio.readString()
        if search(key, a) < 0:
            stdio.writeln(key)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# more emails.txt 
# bob@office
# carl@beach
# marvin@spam
# bob@office
# bob@office
# mallory@spam
# dave@boat
# eve@airport
# alice@home

# more white.txt
# alice@home
# bob@office
# carl@beach
# dave@boat

# python binarysearch.py white.txt < emails.txt 
# marvin@spam
# mallory@spam
# eve@airport

