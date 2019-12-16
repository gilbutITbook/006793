#-----------------------------------------------------------------------
# mm1queue.py
#-----------------------------------------------------------------------

import sys
import stddraw
import stdrandom
from linkedqueue import Queue
from histogram import Histogram

# Accept float command-line arguments lamb and mu. Simulate an
# M/M/1 queue with arrival rate lamb and service rate mu.

lamb = float(sys.argv[1])  # Arrival rate
mu = float(sys.argv[2])    # Service rate

histogram = Histogram(60 + 1)
queue = Queue()
stddraw.setCanvasSize(700, 500)

# Compute time of next arrival.
nextArrival = stdrandom.exp(lamb)

# Compute time of next completed service.
nextService = nextArrival + stdrandom.exp(mu) 

# Simulate the M/M/1 queue.
while True:

    # Next event is an arrival.
    while nextArrival < nextService:
        # Simulate an arrival
        queue.enqueue(nextArrival)
        nextArrival += stdrandom.exp(lamb)

    # Next event is a service completion.
    arrival = queue.dequeue()
    wait = nextService - arrival

    # Update the histogram.
    stddraw.clear(stddraw.LIGHT_GRAY)
    histogram.addDataPoint(min(60, int(round(wait))))
    histogram.draw()
    stddraw.show(20.0)

    # Update the queue.
    if queue.isEmpty():
        nextService = nextArrival + stdrandom.exp(mu)
    else:
        nextService = nextService + stdrandom.exp(mu)


#-----------------------------------------------------------------------

# python mm1queue.py .167 .25

# python mm1queue.py .167 .20

