#-----------------------------------------------------------------------
# quadratic.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# 실수 b와 c를 명령 줄 인자로 받는다.
# 이차방정식 근의 공식을 이용해 방정식 x^2 + bx + c의 근을 구한다.
# 근을 화면에 출력한다.

b = float(sys.argv[1])
c = float(sys.argv[2])

discriminant = b*b - 4.0*c
d = math.sqrt(discriminant)

stdio.writeln((-b + d) / 2.0)
stdio.writeln((-b - d) / 2.0)

#-----------------------------------------------------------------------

# quadratic.py -3.0 2.0
# 2.0
# 1.0

# quadratic.py -1.0 -1.0
# 1.618033988749895
# -0.6180339887498949

# quadratic.py 1.0 1.0
# Traceback (most recent call last):
#   File "quadratic.py", line 17, in <module>
#     d = math.sqrt(discriminant)
# ValueError: math domain error
