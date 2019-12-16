#-----------------------------------------------------------------------
# dragon1.py
#-----------------------------------------------------------------------

import stdio

# 0에서 5차까지의 용 곡선 그리는 명령을 표준 출력 장치에 출력한다.

dragon0 = 'F'
nogard0 = 'F'
dragon1 = dragon0 + 'L' + nogard0
nogard1 = dragon0 + 'R' + nogard0
dragon2 = dragon1 + 'L' + nogard1
nogard2 = dragon1 + 'R' + nogard1
dragon3 = dragon2 + 'L' + nogard2
nogard3 = dragon2 + 'R' + nogard2
dragon4 = dragon3 + 'L' + nogard3
nogard4 = dragon3 + 'R' + nogard3
dragon5 = dragon4 + 'L' + nogard4

stdio.writeln(dragon0)
stdio.writeln(dragon1)
stdio.writeln(dragon2)
stdio.writeln(dragon3)
stdio.writeln(dragon4)
stdio.writeln(dragon5)

#-----------------------------------------------------------------------

# python dragon1.py     
# F
# FLF
# FLFLFRF
# FLFLFRFLFLFRFRF
# FLFLFRFLFLFRFRFLFLFLFRFRFLFRFRF
# FLFLFRFLFLFRFRFLFLFLFRFRFLFRFRFLFLFLFRFLFLFRFRFRFLFLFRFRFLFRFRF
