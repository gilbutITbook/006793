#-----------------------------------------------------------------------
# useargument.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept a name as a command-line argument. Write a message containing
# that name to standard output.

stdio.write('Hi, ')
stdio.write(sys.argv[1])
stdio.writeln('. How are you?')

#-----------------------------------------------------------------------

# python useargument.py Alice
# Hi, Alice. How are you?

# python useargument.py Bob
# Hi, Bob. How are you?

# python useargument.py Carol
# Hi, Carol. How are you?
