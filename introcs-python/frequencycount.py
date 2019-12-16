#-----------------------------------------------------------------------
# frequencycount.py
#-----------------------------------------------------------------------

import sys
import stdio
from counter import Counter

# Read words from standard input, and write the frequency counts
# of the words to standard output.

words = stdio.readAllStrings()

# Previous doesn't eliminate punctuation chars, but this does:
#   import re
#   s = stdio.readAll()
#   regExp = re.compile(r'\w+') # One or more alphanumeric chars
#   words = regExp.findall(s)

words.sort()  # or merge.sort(words)

zipf = []
for i in range(len(words)):
    if (i == 0) or (words[i] != words[i-1]):
        entry = Counter(words[i], len(words))
        zipf += [entry]
    zipf[len(zipf)-1].increment()

zipf.sort()  # or merge.sort(zipf)
zipf.reverse()
for entry in zipf:
    stdio.writeln(entry)

#-----------------------------------------------------------------------

# python frequencycount.py < tomsawyer.txt
# the: 3452
# and: 2908
# a: 1758
# to: 1741
# of: 1539
# was: 1124
# in: 926
# he: 849
# that: 786
# his: 769
# with: 670
# it: 633
# I: 618
# you: 595
# had: 508
# for: 491
# Tom: 427
# they: 392
# The: 374
# ...

# python frequencycount.py < leipzig100k.txt | more
# the: 116512
# of: 59372
# to: 56121
# a: 47399
# and: 43547
# in: 42943
# for: 20692
# The: 19192
# that: 18797
# is: 17205
# said: 14932
# on: 14685
# was: 14169
# with: 11910
# by: 11778
# from: 10747
# at: 10700
# as: 10389
# be: 10269
# he: 9364
# has: 9156
# it: 8999
# have: 8833

# python frequencycount.py < leipzig200k.txt | more
# the: 232333
# of: 118742
# to: 112518
# a: 94685
# and: 87259
# in: 85927
# for: 40963
# The: 38414
# that: 37468
# is: 34556
# said: 29688
# on: 29237
# was: 28240
# by: 23701
# with: 23591
# at: 21414
# from: 21371
# as: 20770
# be: 20247
# he: 18781
# has: 18154
# it: 18121
# have: 17617

# python frequencycount.py < leipzig1m.txt
# the: 1160105
# of: 593492
# to: 560945
# a: 472819
# and: 435866
# in: 430484
# for: 205531
# The: 192296
# that: 188971
# is: 172225
# said: 148915
# on: 147024
# was: 141178
# by: 118429
# with: 118193
# at: 107551
# from: 105921
# as: 104028
# be: 101027
# he: 93393
# it: 90975
# has: 90116
# have: 87856
# ...

