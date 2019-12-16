#-----------------------------------------------------------------------
# potentialgene.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Return True if string dna corresponds to a potential gene, that is,
# if its length is a multiple of 3, it starts with the start codon
# (ATG), it ends with a stop codon (TAA or TAG or TGA), and it has
# no intervening stop codons. Otherwise return FALSE.

def isPotentialGene(dna):
    # number of bases is a multiple of 3
    if (len(dna) % 3) != 0: return False
    # starts with start codon
    if not dna.startswith('ATG'): return False
    # no intervening stop codons
    for i in range(len(dna) - 3):
        if i % 3 == 0:
            if dna[i:i+3] == 'TAA': return False
            if dna[i:i+3] == 'TAG': return False
            if dna[i:i+3] == 'TGA': return False
    # ends with a stop codon
    if dna.endswith('TAA'): return True
    if dna.endswith('TAG'): return True
    if dna.endswith('TGA'): return True
    return False

#-----------------------------------------------------------------------

# Accept a DNA sequence as a comand-line argument. Write to 
# True to standard output if the DNA sequence corresponds to a
# potential gene, and False otherwise.

dna = sys.argv[1]
stdio.writeln(isPotentialGene(dna))

#-----------------------------------------------------------------------

# python potentialgene.py ATGCGCCTGCGTCTGTACTAG
# True

# python potentialgene.py ATGCGCTGCGTCTGTACTAG
# False

