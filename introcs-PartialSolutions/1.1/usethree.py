#-----------------------------------------------------------------------
# usethree.py
#-----------------------------------------------------------------------

import stdio
import sys

# 명령 줄 인자로 이름 세 개를 입력받는다.
# 표준 출력 장치에 "Hi" 다음에 이름 세 개를 역순으로 출력한다.

stdio.write('Hi, ')
stdio.write(sys.argv[3])
stdio.write(', ')
stdio.write(sys.argv[2])
stdio.write(', and ')
stdio.write(sys.argv[1])
stdio.writeln('.')

#-----------------------------------------------------------------------

# python usethree.py Alice Bob Carol
# Hi, Carol, Bob, and Alice.
