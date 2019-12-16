#-----------------------------------------------------------------------
# birthday.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import random

# Compute the number of people (by simulation) that must enter a room
# until two of them share a birthday. Assume birthdays are independent
# and uniform from 0 to 364. Write the number of people to standard
# output.

DAYS_PER_YEAR = 365

# Keep track of the count of people who have entered the room.
peopleCount = 0

# birthdaysSeen[birthday] = True iff someone who has entered the room
# was born on day birthday.
birthdaysSeen = stdarray.create1D(DAYS_PER_YEAR, False)

# Perform the simulation.
while True:
    peopleCount += 1
    birthday = random.randrange(0, DAYS_PER_YEAR)
    if birthdaysSeen[birthday]:
        break # Two people with the same birthday, so break out of loop
    birthdaysSeen[birthday] = True

stdio.writeln(peopleCount)

#-----------------------------------------------------------------------

# python birthday.py
# 38

# python birthday.py
# 20

# python birthday.py
# 11

# python birthday.py
# 18

