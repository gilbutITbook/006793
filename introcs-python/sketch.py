#-----------------------------------------------------------------------
# sketch.py
#-----------------------------------------------------------------------

import sys
import stdio
import stdarray
from vector import Vector

#-----------------------------------------------------------------------

class Sketch:

    # Construct a new Sketch object which is a profile of string
    # text. The profile should consist of a unit vector of dimension
    # d. Element i of the vector should indicate how many k-grams
    # in the file (or web page) hash to i.
    def __init__(self, text, k, d):
        freq = stdarray.create1D(d, 0)
        for i in range(len(text) - k + 1):
            kgram = text[i:i+k]
            h = hash(kgram)
            freq[h % d] += 1
        vector = Vector(freq)
        self._sketch = vector.direction()  # Unit vector

    # Return the similarity measure between self and Sketch object
    # other as a number between 0 and 1. 0 indicates that the
    # objects are dissimilar; 1 indicates that they are similar.
    def similarTo(self, other):
        return self._sketch.dot(other._sketch)

    # Return a string representation of self.
    def __str__(self):
        return str(self._sketch)

#-----------------------------------------------------------------------

# For testing.
# Accept integers k and d as command-line arguments. Read text from
# standard input, and construct a Sketch object from that text, k, and
# d. Write the Sketch object to standard output.

def main():
    text = stdio.readAll()
    k = int(sys.argv[1])
    d = int(sys.argv[2])
    sketch = Sketch(text, k, d)
    stdio.writeln(sketch)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# more genome20.txt 
# ATAGATGCATAGCGCATAGC

# python sketch.py 2 16 < genome20.txt 
# [0.37210420376762543, 0.37210420376762543, 0.49613893835683387, 
# 0.0, 0.12403473458920847, 0.0, 
# 0.0, 0.0, 0.0, 
# 0.0, 0.24806946917841693, 0.0, 
# 0.12403473458920847, 0.6201736729460423, 0.0, 0.0]

