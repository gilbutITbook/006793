#-----------------------------------------------------------------------
# windchill.py
#-----------------------------------------------------------------------

import stdio
import sys

# 화씨 온도(t)와 풍속(v)을 명령 줄 인자로 받는다.
# 기상청의 공식을 이용해 체감 온도를 계산하고 출력한다.
# 참조 : http://www.nws.noaa.gov/om/windchill/index.shtml

t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)

stdio.writeln('Temperature = ' + str(t))
stdio.writeln('Wind speed  = ' + str(v))
stdio.writeln('Wind chill  = ' + str(w))

#-----------------------------------------------------------------------

# python windchill.py 32 10
# Temperature = 32.0
# Wind speed  = 10.0
# Wind chill  = 23.72714425963738

