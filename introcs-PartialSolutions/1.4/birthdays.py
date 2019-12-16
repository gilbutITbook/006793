#-----------------------------------------------------------------------
# birthdays.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys
import random

# Accept an integer command-line argument n. Compute the number of
# people (by simulation) that must enter a room until two of them
# share a birthday. Assume birthdays are independent
# and uniform from 0 to 364. Repeat the experiment n times, and write
# the average number of people to standard output.

DAYS_PER_YEAR = 365

n = int(sys.argv[1])

# Keep track of the count of people who have entered the room.
peopleCount = 0

for i in range(n):

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

stdio.writeln(float(peopleCount)/float(n))

#-----------------------------------------------------------------------

# python birthdays.py 1
# 26.0

# python birthdays.py 10
# 24.0

# python birthdays.py 100
# 26.79

# python birthdays.py 1000
# 24.581

# python birthdays.py 10000
# 24.8073

# python birthdays.py 100000
# 24.57607
