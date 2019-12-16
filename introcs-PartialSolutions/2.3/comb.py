#-----------------------------------------------------------------------
# comb.py
#-----------------------------------------------------------------------

import stdio
import sys

#-----------------------------------------------------------------------

# Return a list containing strings which are the length k combinations
# of the letters of string s.

def choose(s, k):
    if k == 0:
        return ['']
    strings = []
    for i in range(len(s)):
        subStrings = choose(s[i+1:], k-1)
        for subString in subStrings:
            strings += [s[i] + subString]
    return strings

#-----------------------------------------------------------------------

# Write each string within list strings to standard output.

def writeStrings(strings):
    for s in strings:
        if s == '':
            stdio.writeln('empty')
        else:
            stdio.writeln(s)
    stdio.writeln()

#-----------------------------------------------------------------------

# Accept integer command-line arguments n and k. Write to standard
# output all length k combinations of the first n characters of the
# alphabet.

def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = alphabet[:n]
    strings = choose(string, k)
    writeStrings(strings)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python comb.py 5 3
# abc
# abd
# abe
# acd
# ace
# ade
# bcd
# bce
# bde
# cde

