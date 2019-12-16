#-----------------------------------------------------------------------
# binaryconverter.py
#-----------------------------------------------------------------------

import stdio
import sys

#-----------------------------------------------------------------------

# Write to standard output the binary representation of n.

def convert(n):
    if n == 0:
        return
    convert(n // 2)
    stdio.write(n % 2)

#-----------------------------------------------------------------------

# Accept positive integer command-line argument n. Write to standard
# output the binary representation of n.

def main():
    n = int(sys.argv[1])
    convert(n)
    stdio.writeln()

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python binaryconverter.py 1
# 1

# python binaryconverter.py 2
# 10

# python binaryconverter.py 10
# 1010

# python binaryconverter.py 100
# 1100100
