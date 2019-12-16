#-----------------------------------------------------------------------
# sumoftwodice.py
#-----------------------------------------------------------------------

import stdio
import random

# 주사위를 두 번 굴려 나온 숫자의 합을 출력한다.

SIDES = 6

a = random.randrange(1, SIDES+1)
b = random.randrange(1, SIDES+1)

total = a + b

stdio.writeln(total)

#-----------------------------------------------------------------------

# python sumoftwodice.py
# 5

# python sumoftwodice.py
# 7

# python sumoftwodice.py
# 10

# python sumoftwodice.py
# 7
