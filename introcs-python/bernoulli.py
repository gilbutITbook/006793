#-----------------------------------------------------------------------
# bernoulli.py
#-----------------------------------------------------------------------

import sys
import math
import stdarray
import stddraw
import stdrandom
import stdstats
import gaussian

#-----------------------------------------------------------------------

# Accept integers n and trials as command-line arguments.
# Perform trials experiments, each of which counts the number
# of heads found when a fair coin is flipped n times. Then
# draw the results to standard draw. Also draw the predicted Gaussian
# distribution function, thereby allowing easy comparison of the
# experimental results to the theoretically predicted results.

n = int(sys.argv[1])
trials = int(sys.argv[2])

freq = stdarray.create1D(n+1, 0)
for t in range(trials):
    heads = stdrandom.binomial(n, 0.5)
    freq[heads] += 1
    
norm = stdarray.create1D(n+1, 0.0)
for i in range(n+1):
    norm[i] = 1.0 * freq[i] / trials
    
phi = stdarray.create1D(n+1, 0.0)
stddev = math.sqrt(n)/2.0
for i in range(n+1):
    phi[i] = gaussian.pdf(i, n/2.0, stddev)
    
stddraw.setCanvasSize(1000, 400)
stddraw.setYscale(0, 1.1 * max(max(norm), max(phi)))
stdstats.plotBars(norm)
stdstats.plotLines(phi)
stddraw.show()

#-----------------------------------------------------------------------

# python bernoulli.py 20 100000

