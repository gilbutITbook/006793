#-----------------------------------------------------------------------
# permutations.py
#-----------------------------------------------------------------------

import stdio
import sys

#-----------------------------------------------------------------------

# Return a list of strings, each of which is a permutation of string s.

def perm(s):
    if len(s) == 0:
        return ['']

    strings = []
    for i in range(len(s)):
        # Compute a list of permutations of s with s[i] removed.
        subStrings = perm(s[:i]+s[i+1:])

        # Prepend s[i] to each string in that list.
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

# Accept integer command-line argument n. Write to standard output
# all permutations of the first n characters of the alphabet.

def main():
    n = int(sys.argv[1])
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = ALPHABET[:n]
    strings = perm(string)
    writeStrings(strings)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python permutations.py 3
# abc
# acb
# bac
# bca
# cab
# cba

