#-----------------------------------------------------------------------
# sine.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# 명령 줄 인자로 실수 x를 입력받는다.
# 테일러 급수 sin x = x - x^3/3! + x^5/5! - x^7/7! + ...를 이용해 sin(x)를 계산한다.
# 결과를 표준 출력 장치에 출력한다.

x = float(sys.argv[1])

# sin(x) = sin(x + 2 PI) 등치성을 이용해 x를 -2 PI와 2 PI 사이의 값으로 변환한다.
twoPi = 2 * math.pi
while x > twoPi:
    x -= twoPi
while x < twoPi:
    x += twoPi

# 다른 방법 :
# x = x % (2 * math.pi)   # %는 실수에 사용할 수 있다!
# 테일러 급수를 계산한다.
term = 1.0      # i번째 term = x^i / i!
total = 0.0     # 테일러 급수에서 처음 i번째 항목까지의 합계

i = 1
while term != 0.0:
    term *= (x / float(i))
    if i % 4 == 1:
        total += term
    if i % 4 == 3:
        total -= term
    i += 1

stdio.writeln(total)

#-----------------------------------------------------------------------

# python sine.py 0 
# 4.372542542582082e-15

# python sine.py 1.5707963267948966
# 1.0000000000000304

# python sine.py 3.141592653589793
# 6.830582986146365e-14

