#-----------------------------------------------------------------------
# combinations.py
#-----------------------------------------------------------------------

import stdio
import sys

#-----------------------------------------------------------------------

# Return a list containing strings which are the combinations of the
# letters of string s, of any length.

def combinations(s):
    strings = []
    for i in range(len(s)+1):
        strings += combinationsOfLength(s, i)
    return strings

#-----------------------------------------------------------------------

# Return a list containing strings which are the length k combinations
# of the letters of string s.

def combinationsOfLength(s, k):
    if k == 0:
        return ['']
    strings = []
    for i in range(len(s)):
        subStrings = combinationsOfLength(s[i+1:], k-1)
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

# Accept integer command-line argument n. Write to standard
# output all combinations of the first n characters of the
# alphabet of any length.

def main():
    n = int(sys.argv[1])

    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = ALPHABET[:n]
    strings = combinations(string)
    writeStrings(strings)

if __name__ == '__main__':
    main()
   

#-----------------------------------------------------------------------

# python combinations.py 4 
# empty
# a
# b
# c
# d
# ab
# ac
# ad
# bc
# bd
# cd
# abc
# abd
# acd
# bcd
# abcd

