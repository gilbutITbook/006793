#-----------------------------------------------------------------------
# playthattune.py
#-----------------------------------------------------------------------

import math
import stdio
import stdarray
import stdaudio

# Read sound samples from standard input, and play the sound to
# standard audio.

SPS = 44100
CONCERT_A = 440.0
NOTES_ON_SCALE = 12.0

while not stdio.isEmpty():

    pitch = stdio.readInt()
    duration = stdio.readFloat()
    hz = CONCERT_A * (2.0 ** (pitch / NOTES_ON_SCALE))
    n = int(SPS * duration)
    note = stdarray.create1D(n+1, 0.0)
    for i in range(n+1):
        note[i] = math.sin(2.0 * math.pi * i * hz / SPS)
    stdaudio.playSamples(note)

stdaudio.wait()

#-----------------------------------------------------------------------

# python playthattune.py < elise.txt

# python playthattune.py < ascale.txt

# python playthattune.py < entertainer.txt

# python playthattune.py < firstcut.txt

# python playthattune.py < freebird.txt

# python playthattune.py < looney.txt

# python playthattune.py < stairwaytoheaven.txt

