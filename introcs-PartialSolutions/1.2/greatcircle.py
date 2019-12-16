#-----------------------------------------------------------------------
# greatcircle.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# 두 점의 위도와 경도를 명령 줄 인자로 입력받는다(x1, y1, x2, y2. 도 단위)
# 두 점 간의 대원 거리를 표준 출력 장치에 출력한다(해리 단위)

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# 사용할 공식이 라디안 단위로 받으므로, 도 단위를 라디안 단위로 변환한다.

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

# 코사인 법칙을 이용해 계산한다.

# 라디안 단위로 계산하는 대원 거리
angle1 = math.acos(math.sin(x1) * math.sin(x2) \
         + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# 다시 도 단위로 변환한다.
angle1 = math.degrees(angle1)

# 지표면 대원 위에서 1도는 60 해리이다.
distance1 = 60.0 * angle1

stdio.writeln(str(distance1) + ' nautical miles')

# 하버사인 공식을 이용해 계산한다.

a = math.sin((x2-x1)/2.0) ** 2.0 \
    + (math.cos(x1) * math.cos(x2) * (math.sin((y2-y1)/2.0) ** 2.0))

# 라디안으로 표현한 대원 거리
angle2 = 2.0 * math.asin(min(1.0, math.sqrt(a)))

# 다시 도 단위로 변환한다.
angle2 = math.degrees(angle2)

# 지표면 대원에서 1도는 60 해리를 나타낸다.
distance2 = 60.0 * angle2

stdio.writeln(str(distance2) + ' nautical miles')

#-----------------------------------------------------------------------

# Leningrad to SF

# python greatcircle.py 59.9 -30.3 37.8 122.4
# 4784.369673474519 nautical miles
# 4784.369673474519 nautical miles
#
# Paris to Austin

# python greatcircle.py 48.87 -2.33 30.27 97.74
# 4423.14075970742 nautical miles
# 4423.140759707421 nautical miles
#
# Nashville airport (BNA) to LAX

# python greatcircle.py 36.12 -86.67 33.94 -118.4
# 1557.505111036951 nautical miles
# 1557.5051110369507 nautical miles
#
# Princeton to Paris

# python greatcircle.py 40.35 74.65 48.87 -2.33
# 3185.1779271158425 nautical miles
# 3185.1779271158416 nautical miles

