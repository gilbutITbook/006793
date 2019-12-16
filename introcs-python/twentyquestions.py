#-----------------------------------------------------------------------
# twentyquestions.py
#-----------------------------------------------------------------------

import stdio
import random

# Generate a random integer. Repeatedly read user guesses from
# standard input. Write 'Too low' or 'Too high' to standard output,
# as appropriate, in response to each guess. Write 'You win!' to
# standard output and exit when the user's guess is correct.

RANGE = 1000000

secret = random.randrange(1, RANGE+1)
stdio.write('I am thinking of a secret number between 1 and ')
stdio.writeln(RANGE)
guess = 0
while guess != secret:
    # Solicit one guess and provide one answer.
    stdio.write('What is your guess? ')
    guess = stdio.readInt()
    if (guess < secret):
        stdio.writeln('Too low')
    elif (guess > secret):
        stdio.writeln('Too high')
    else:
        stdio.writeln('You win!')
        
#-----------------------------------------------------------------------

# python twentyquestions.py
# I am thinking of a secret number between 1 and 1000000
# What is your guess? 500000
# Too low
# What is your guess? 750000     
# Too high
# What is your guess? 625000
# Too high
# What is your guess? 562500
# Too high
# What is your guess? 531250
# Too high
# What is your guess? 515625
# Too high
# What is your guess? 507812
# Too high
# What is your guess? 503906
# Too high
# What is your guess? 501953
# Too high
# What is your guess? 500977
# Too low
# What is your guess? 501465
# Too low
# What is your guess? 501709
# Too high
# What is your guess? 501587
# Too low
# What is your guess? 501648
# Too low
# What is your guess? 501679
# Too low
# What is your guess? 501694
# Too high
# What is your guess? 501686
# You win!

