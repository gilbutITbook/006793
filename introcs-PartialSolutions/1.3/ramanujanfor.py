#-----------------------------------------------------------------------
# ramanujanfor.py
#-----------------------------------------------------------------------

import stdio
import sys
    
# 명령 줄 인자로 정수 n을 입력받는다.
# 1에서 n 사이의 숫자 중, 두 가지 이상의 방법으로 제곱의 합으로 표현할 수 있는 수를 출력한다.
# 버그 : 두 가지 이상의 방법으로 표현할 수 있는 수는 중복 출력된다.

# 명령 줄에서 인자를 하나 입력받는다.
n = int(sys.argv[1])

# 각 a, b, c, d에 대해 a^3 + b^3 = c^3 + d^3인지 확인한다.
for a in range(1, n+1):
    a3 = a*a*a
    if a3 > n:
        break

    # 중복된 것을 출력하지 않도록 a에서 시작한다.
    for b in range(a, n+1):
        b3 = b*b*b
        if a3 + b3 > n:
            break;

        # 중복된 것을 출력하지 않도록 a+1에서 시작한다.
        for c in range(a+1, n+1):
            c3 = c*c*c
            if c3 > a3 + b3:
                break

            # 중복된 것을 출력하지 않도록 c에서 시작한다.
            for d in range(c, n+1):
                d3 = d*d*d
                if c3 + d3 > a3 + b3:
                    break

                if c3 + d3 == a3 + b3:
                    stdio.write(str(a3+b3) + ' = ')
                    stdio.write(str(a) + '^3 + ' + str(b) + '^3 = ')
                    stdio.write(str(c) + '^3 + ' + str(d) + '^3')
                    stdio.writeln()

#-----------------------------------------------------------------------

# python3 ramanujanfor.py 2000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3

# python3 ramanujanfor.py 10000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3
# 4104 = 2^3 + 16^3 = 9^3 + 15^3
