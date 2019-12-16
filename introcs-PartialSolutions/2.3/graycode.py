#-----------------------------------------------------------------------
# graycode.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Return an n-bit Gray code.

def genCode(n):
    if n == 0:
        return ['']
    
    code1 = genCode(n-1)
    code2 = []
    for codeWord in code1:
        code2 = [codeWord] + code2
        
    for i in range(len(code1)):
        code1[i] += '0'
    for i in range(len(code2)):
        code2[i] += '1'
    return code1 + code2    
    
#-----------------------------------------------------------------------

# Accept integer n, and write to standard output an n-bit Gray code.

def main():
    n = int(sys.argv[1])
    code = genCode(n)
    for codeWord in code:
        stdio.writeln(codeWord)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python graycode.py 1
# 0
# 1

# python graycode.py 2
# 00
# 10
# 11
# 01

# python graycode.py 3
# 000
# 100
# 110
# 010
# 011
# 111
# 101
# 001

# python graycode.py 4
# 0000
# 1000
# 1100
# 0100
# 0110
# 1110
# 1010
# 0010
# 0011
# 1011
# 1111
# 0111
# 0101
# 1101
# 1001
# 0001
