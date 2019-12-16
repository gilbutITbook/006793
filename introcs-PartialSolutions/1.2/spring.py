#-----------------------------------------------------------------------
# spring.py
#-----------------------------------------------------------------------

import stdio
import sys

# 월과 일을 명령 줄 인자로 입력받는다.
# 날짜가 봄이면 True를 출력한다.

month = int(sys.argv[1])
day =   int(sys.argv[2])

isSpring = (month == 3 and day >= 20 and day <= 31) or \
           (month == 4 and day >=  1 and day <= 30) or \
           (month == 5 and day >=  1 and day <= 31) or \
           (month == 6 and day >=  1 and day <= 20)

stdio.writeln(isSpring)

#-----------------------------------------------------------------------

# python spring.py 1 1 
# False

# python spring.py 3 19
# False

# python spring.py 3 20
# True

# python spring.py 6 20
# True

# python spring.py 6 21
# False

# python spring.py 12 31
# False

