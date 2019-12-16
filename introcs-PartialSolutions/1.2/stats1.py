#-----------------------------------------------------------------------
# stats1.py
#-----------------------------------------------------------------------

import stdio
import random

# 0.0과 1.0 사이의 실수형 난수 5개를 생성한다.
# 생성된 난수와, 이들의 평균값, 최솟값, 최댓값을 출력한다.

N = 5

# 난수 5개를 생성한다.
x1 = random.random()
x2 = random.random()
x3 = random.random()
x4 = random.random()
x5 = random.random()

# 난수 5개를 출력한다.
stdio.writeln(x1)
stdio.writeln(x2)
stdio.writeln(x3)
stdio.writeln(x4)
stdio.writeln(x5)

# 최댓값, 최솟값, 평균을 구한다.
minimum = min(x1, x2, x3, x4, x5)
maximum = max(x1, x2, x3, x4, x5)
average = (x1 + x2 + x3 + x4 + x5) / N

# 계산 결과를 출력한다.
stdio.writeln('Average = ' + str(average))
stdio.writeln('Min     = ' + str(minimum))
stdio.writeln('Max     = ' + str(maximum))

#-----------------------------------------------------------------------

# python stats1.py      
# 0.556496926354658
# 0.513350209165622
# 0.2388414489512366
# 0.6624155966015689
# 0.9627794290136971
# Average = 0.5867767220173565
# Min     = 0.2388414489512366
# Max     = 0.9627794290136971

# python stats1.py
# 0.6478938018093143
# 0.4962425246577342
# 0.4813720971364449
# 0.3713682192048282
# 0.22171061570089612
# Average = 0.44371745170184357
# Min     = 0.22171061570089612
# Max     = 0.6478938018093143

