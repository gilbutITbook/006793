#-----------------------------------------------------------------------
# threesort.py
#-----------------------------------------------------------------------

import stdio
import sys

# 명령 줄 인자로 세 개의 정수를 입력받는다.

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

# 값을 계산한다.
minimum = min(a, b, c)
maximum = max(a, b, c)
median = a + b + c - minimum - maximum;

# 결과를 출력한다.
stdio.writeln(minimum)
stdio.writeln(median)
stdio.writeln(maximum)

#-----------------------------------------------------------------------

# python threesort.py 18 25 74
# 18
# 25
# 74

# python threesort.py 74 18 25
# 18
# 25
# 74

