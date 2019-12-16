#-----------------------------------------------------------------------
# compareadocuments.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stdio
from instream import InStream
from sketch import Sketch

#-----------------------------------------------------------------------

# Accept integers k and d as command-line arguments. Read a document
# list from standard input, compute profiles based on k-gram
# frequencies for all the documents, and write a matrix of similarity
# measures between all pairs of documents. d is the dimension of the
# profiles.

k = int(sys.argv[1])
d = int(sys.argv[2])

filenames = stdio.readAllStrings()
sketches = stdarray.create1D(len(filenames))

for i in range(len(filenames)):
    text = InStream(filenames[i]).readAll()
    sketches[i] = Sketch(text, k, d)
    
stdio.write('    ')
for i in range(len(filenames)):
    stdio.writef('%8.4s', filenames[i])
stdio.writeln()

for i in range(len(filenames)):
    stdio.writef('%.4s', filenames[i])
    for j in range(len(filenames)):
        stdio.writef('%8.2f', sketches[i].similarTo(sketches[j]))
    stdio.writeln()
    
#-----------------------------------------------------------------------

# more documents.txt 
# constitution.txt
# tomsawyer.txt
# huckfinn.txt
# prejudice.txt
# vector.py
# djia.csv
# amazon.html
# actg.txt

# $ python comparedocuments.py 5 10000 < documents.txt 
#         cons    toms    huck    prej    vect    djia    amaz    actg
# cons    1.00    0.69    0.63    0.67    0.09    0.15    0.19    0.12
# toms    0.69    1.00    0.93    0.89    0.07    0.18    0.19    0.14
# huck    0.63    0.93    1.00    0.83    0.05    0.16    0.16    0.13
# prej    0.67    0.89    0.83    1.00    0.06    0.20    0.20    0.14
# vect    0.09    0.07    0.05    0.06    1.00    0.02    0.19    0.02
# djia    0.15    0.18    0.16    0.20    0.02    1.00    0.11    0.07
# amaz    0.19    0.19    0.16    0.20    0.19    0.11    1.00    0.06
# actg    0.12    0.14    0.13    0.14    0.02    0.07    0.06    1.00
