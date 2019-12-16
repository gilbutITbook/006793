#-----------------------------------------------------------------------
# gambler.py
#-----------------------------------------------------------------------

import stdio
import sys
import random

# Accept integer command-line arguments stake, goal, and trialCount.
# Run trialCount experiments that start with stake dollars and
# terminate on 0 dollars or goal.  Write to standard output the
# percentage of wins and the average number of bets per experiment.

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])

# Run trialCount experiments that start with stake and terminate on
# 0 or goal.
bets = 0
wins = 0
for t in range(trials):
    # Run one experiment.
    cash = stake
    while cash > 0 and cash < goal:
        # Simulate one bet.
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

stdio.writeln(str(100 * wins//trials) + '% wins')
stdio.writeln('Avg # bets: ' + str(bets//trials))

#-----------------------------------------------------------------------

# python gambler.py 10 20 1000
# 49% wins
# Avg # bets: 99

# python gambler.py 50 250 100
# 21% wins
# Avg # bets: 12712

# python gambler.py 500 2500 100
# 21% wins
# Avg # bets: 1002424

