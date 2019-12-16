#-----------------------------------------------------------------------
# tenhellos.py
#-----------------------------------------------------------------------

import stdio

# Write 10 Hellos to standard output.

stdio.writeln('1st Hello')
stdio.writeln('2nd Hello')
stdio.writeln('3rd Hello')

i = 4
while i <= 10:
    stdio.writeln(str(i) + 'th Hello')
    i = i + 1
    
#-----------------------------------------------------------------------

# python tenhellos.py
# 1st Hello
# 2nd Hello
# 3rd Hello
# 4th Hello
# 5th Hello
# 6th Hello
# 7th Hello
# 8th Hello
# 9th Hello
# 10th Hello
