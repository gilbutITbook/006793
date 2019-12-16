#-----------------------------------------------------------------------
# polar.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# 명령 줄 인자로 실수 x, y를 받는다.
# 직교 좌표(x, y)를 극좌표(r, theta)로 변환한 후 r과 theta를 표준 출력장치에 출력한다.
x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.sqrt(x*x + y*y)
theta = math.atan2(y, x)

stdio.writeln('r     = ' + str(r))
stdio.writeln('theta = ' + str(theta))

#-----------------------------------------------------------------------

# python polar.py 0.0 0.0
# r     = 0.0
# theta = 0.0

# python polar.py 0.0 1.0
# r     = 1.0
# theta = 1.5707963267948966

# python polar.py 1.0 0.0 
# r     = 1.0
# theta = 0.0

# python polar.py 1.0 1.0
# r     = 1.4142135623730951
# theta = 0.7853981633974483

# python polar.py 0.0 -1.0
# r     = 1.0
# theta = -1.5707963267948966

# python polar.py -1.0 0.0
# r     = 1.0
# theta = 3.141592653589793

# python polar.py -1.0 -1.0
# r     = 1.4142135623730951
# theta = -2.356194490192345

