#-----------------------------------------------------------------------
# montehall.py
#-----------------------------------------------------------------------

import stdio
import sys
import random

# 명령 줄에서 정수 n을 입력받는다.
# 선택을 바꿔 게임을 n번 수행한 후 승률을 화면에 출력한다.
# 주의 : 실제 상을 받을 확률은 2/3이다.
n = int(sys.argv[1])  # 시도 횟수
wins = 0              # 선택을 바꿨을 때 상을 받은 횟수

# 실험을 n번 반복한다.
for i in range(0, n):

    # 진행자는 문1에서 문3에 고르게 무작위로 상을 숨긴다.
    prize  = random.randrange(0, 3)

    # 도전자는 1에서 3까지의 문을 무작위로 선택한다.
    choice = random.randrange(0, 3)

    # 진행자는 선택하지 않은 문 중 상이 없는 문을 무작위로 고른다.
    reveal = random.randrange(0, 3)
    while (reveal == choice) or (reveal == prize):
        reveal = random.randrange(0, 3)

    # 사용자가 선택을 바꾼 문을 계산한다.
    other = 0 + 1 + 2 - reveal - choice

    # 선택을 바꿔서 상을 받았는가?
    if other == prize:
        wins += 1

# 확률을 계산하기 위해 실수로 변환해 나눈다.
fractionWon = float(wins) / float(n)

# 결과를 출력한다.
stdio.writeln('상 받을 확률 : ' + str(fractionWon))

#-----------------------------------------------------------------------

# python3 montehall.py 100
# 상 받을 확률 : 0.62

# python3 montehall.py 1000
# 상 받을 확률 : 0.666

# python3 montehall.py 10000
# 상 받을 확률 : 0.6562

# python3 montehall.py 100000
# 상 받을 확률 : 0.6697
