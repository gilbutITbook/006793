#-----------------------------------------------------------------------
# clock.py
#-----------------------------------------------------------------------

import stddraw
import math

# Draw an animation of the second, minute, and hour hands of an
# analog clock.
t = 0
time = '0:00:00'
oldTime = '0:00:00'
while True:

    # Remainder operator with floats so all hands move every second.
    seconds = t % 60
    minutes = (t / 60.0) % 60
    hours   = (t / 3600.0) % 12

    #stddraw.clear()
    #stddraw.setPenRadius()

    # Draw clock face.
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(0.5, 0.5, 0.45)

    # Draw hour markers.
    stddraw.setPenColor(stddraw.BLUE)
    for i in range(12):
        theta = math.radians(i * 30)
        stddraw.filledCircle(0.5 + 0.4 * math.cos(theta), \
                             0.5 + 0.4 * math.sin(theta), .025)

    # Draw second hand.
    stddraw.setPenRadius(.01)
    stddraw.setPenColor(stddraw.YELLOW)
    angle1 = math.radians(6 * seconds)
    r1 = 0.4
    stddraw.line(0.5, 0.5, \
                 0.5 + r1 * math.sin(angle1), \
                 0.5 + r1 * math.cos(angle1))

    # Draw minute hand.
    stddraw.setPenRadius(.02)
    stddraw.setPenColor(stddraw.GRAY)
    angle2 = math.radians(6 * minutes)
    r2 = 0.3
    stddraw.line(0.5, 0.5, \
                 0.5 + r2 * math.sin(angle2), \
                 0.5 + r2 * math.cos(angle2))

    # Draw hour hand.
    stddraw.setPenRadius(.025)
    stddraw.setPenColor(stddraw.WHITE)
    angle3 = math.radians(30 * hours)
    r3 = 0.2
    stddraw.line(0.5, 0.5, \
                 0.5 + r3 * math.sin(angle3), \
                 0.5 + r3 * math.cos(angle3))

    # Draw digital time.
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0.5, 0.02, oldTime)
    oldTime = time
    second = t          % 60
    minute = (t / 60)   % 60
    hour   = (t / 3600) % 12
    time = '%2d:%02d:%02d' % (hour, minute, second)
    stddraw.setPenColor(stddraw.RED)
    stddraw.text(0.5, 0.02, time)

    # 1000 miliseconds = 1 second
    stddraw.show(1000.0)
    t += 1

#-----------------------------------------------------------------------

# python clock.py

