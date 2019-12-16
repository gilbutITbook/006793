#-----------------------------------------------------------------------
# perm.py
#-----------------------------------------------------------------------

import stdio
import sys

#-----------------------------------------------------------------------

# Return a list of strings, each of which is a length k permutation
# of string s.

def perm(s, k):

    if k == 0:
        return ['']

    if k > len(s):
        return []

    # Recursive step.
    strings = []
    for i in range(len(s)):
        # Compute a list of length k-1 permutations of s with
        # s[i] removed.
        subStrings = perm(s[:i]+s[i+1:], k-1)

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

# Accept integer command-line arguments n and k. Write to standard
# output all length k permutations of the first n characters of the
# alphabet.

def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])

    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = ALPHABET[:n]
    strings = perm(string, k)
    writeStrings(strings)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------
    
# python perm.py 4 2
# ab
# ac
# ad
# ba
# bc
# bd
# ca
# cb
# cd
# da
# db
# dc

