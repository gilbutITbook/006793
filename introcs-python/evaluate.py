#-----------------------------------------------------------------------
# evaluate.py
#-----------------------------------------------------------------------

import stdio
import math
from arraystack import Stack

#-----------------------------------------------------------------------

# Read a fully parenthesized numeric expression from standard input,
# evaluate it, and write the resulting number to standard output.

ops = Stack()
values = Stack()

while not stdio.isEmpty():
    token = stdio.readString()
    if   token == '+':    ops.push(token)
    elif token == '-':    ops.push(token)
    elif token == '*':    ops.push(token)
    elif token == 'sqrt': ops.push(token)
    elif token == ')':
        # Pop, evaluate, and push result.
        op = ops.pop()
        value = values.pop()
        if   op == '+':    value = values.pop() + value
        elif op == '-':    value = values.pop() - value
        elif op == '*':    value = values.pop() * value
        elif op == 'sqrt': value = math.sqrt(value)
        values.push(value)
    elif token != '(':
        # Token not operator or paren, so push float value.
        values.push(float(token))
stdio.writeln(values.pop())

#-----------------------------------------------------------------------

# more expression1.txt
# ( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )

# python evaluate.py < expression1.txt 
# 101.0

# more expression2.txt
# ( ( 1 + sqrt ( 5.0 ) ) * 0.5 )

# python evaluate.py < expression2.txt 
# 1.618033988749895

