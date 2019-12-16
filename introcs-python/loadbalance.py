#-----------------------------------------------------------------------
# loadbalance.py
#-----------------------------------------------------------------------

import sys
import stddraw
import stdstats
from linkedqueue import Queue
from randomqueue import RandomQueue

# Accept integers serverCount, itemCount, and sampleSize as
# command-line arguments. Simulate the process of assigning
# itemCount items to a set of serverCount servers. Put requests
# on the shortest of a sample of sampleSize queues chosen at random.

serverCount = int(sys.argv[1])
itemCount = int(sys.argv[2])
sampleSize = int(sys.argv[3])

# Create a RandomQueue object containing Queue objects.
servers = RandomQueue()
for i in range(serverCount):
    servers.enqueue(Queue())

for j in range(itemCount):
    # Assign an item to a server.
    best = servers.sample()
    for k in range(1, sampleSize):
        # Pick a random server, update if new best.
        queue = servers.sample()
        if len(queue) < len(best):
            best = queue
    # best is the shortest server queue.
    best.enqueue(j)

lengths = []
while not servers.isEmpty():
    lengths += [len(servers.dequeue())]
stddraw.clear(stddraw.LIGHT_GRAY)
stddraw.setYscale(0, 2.0*itemCount/serverCount)
stdstats.plotBars(lengths)
stddraw.show()

#-----------------------------------------------------------------------

# python loadbalance.py 50 500 1

# python loadbalance.py 50 500 2

