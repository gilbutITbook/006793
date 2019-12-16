#-----------------------------------------------------------------------
# gaussiantable.py
#-----------------------------------------------------------------------

import sys
import stdio
import gaussian

#-----------------------------------------------------------------------

# Accept a mean and standard deviation as command-line arguments.
# Write to standard output a table of the percentage of students
# scoring below certain scores on the SAT, assuming the test scores
# obey a Gaussian  distribution with the given mean and standard
# deviation.

mu = float(sys.argv[1])
sigma = float(sys.argv[2])

for score in range(400, 1600+1, 100):
    percent = gaussian.cdf(score, mu, sigma)
    stdio.writef('%4d  %.4f\n', score, percent)
 
#-----------------------------------------------------------------------

# python gaussiantable.py 1019 209
#  400  0.0015
#  500  0.0065
#  600  0.0225
#  700  0.0635
#  800  0.1474
#  900  0.2845
# 1000  0.4638
# 1100  0.6508
# 1200  0.8068
# 1300  0.9106
# 1400  0.9658
# 1500  0.9893
# 1600  0.9973
