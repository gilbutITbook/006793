#-----------------------------------------------------------------------
# floatops.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept two floats a and b as command-line arguments. Use them
# to illustrate float operators. Write the results to standard output.

a = float(sys.argv[1])
b = float(sys.argv[2])

total = a + b
diff  = a - b
prod  = a * b
quot  = a / b
exp   = a ** b

stdio.writeln(str(a) + ' +  ' + str(b) + ' = ' + str(total))
stdio.writeln(str(a) + ' -  ' + str(b) + ' = ' + str(diff))
stdio.writeln(str(a) + ' *  ' + str(b) + ' = ' + str(prod))
stdio.writeln(str(a) + ' /  ' + str(b) + ' = ' + str(quot))
stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(exp))

#-----------------------------------------------------------------------

# python floatops.py 123.456 78.9
# 123.456 +  78.9 = 202.356
# 123.456 -  78.9 = 44.556
# 123.456 *  78.9 = 9740.6784
# 123.456 /  78.9 = 1.5647148289
# 123.456 ** 78.9 = 1.04788279167e+165
