#-----------------------------------------------------------------------
# kamasutra.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept two strings as command-line arguments to be used as key
# strings in a Kama Sutra cipher. Then repeatedly read a line from 
# standard input, encode it using the cipher, and write the result
# to standard output.
    
top = sys.argv[1]
bot = sys.argv[2]

while stdio.hasNextLine():
    line = stdio.readLine()
    for c in line:
        if top.find(c) >= 0:
            stdio.write(bot[top.find(c)])
        elif bot.find(c) >= 0:
            stdio.write(top[bot.find(c)])
        else:
            stdio.write(c)
    stdio.writeln()
    
#-----------------------------------------------------------------------
   
# python kamasutra.py THEQUICKBROWNFOX FXJMPSVLAZYDG
# MEET AT ELEVEN
# QJJF BF JKJCJG
# Ctrl-d

