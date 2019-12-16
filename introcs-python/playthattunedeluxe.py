#-----------------------------------------------------------------------
# playthattune.py
#-----------------------------------------------------------------------

import math
import stdio
import stdarray
import stdaudio

#-----------------------------------------------------------------------

# Superpose arrays a and b, weighted by aWeight and bWeight.

def superpose(a, b, aWeight, bWeight):
    c = stdarray.create1D(len(a), 0.0)
    for i in range(len(a)):
        c[i] = a[i]*aWeight + b[i]*bWeight
    return c

#-----------------------------------------------------------------------

# Return an array to play a note with frequency hz for
# duration t.

def tone(hz, t):
    SPS = 44100
    n = int(SPS * t)
    a = stdarray.create1D(n+1, 0.0)
    for i in range(n+1):
        a[i] = math.sin(2.0 * math.pi * i * hz / SPS)
    return a

#-----------------------------------------------------------------------

# Return an array to play a note with the given pitch
# with harmonics for duration t.

def note(pitch, t):
    CONCERT_A_HZ = 440.0
    NOTES_ON_SCALE = 12.0
    hz = CONCERT_A_HZ * (2.0 ** (pitch / NOTES_ON_SCALE))
    a = tone(hz, t)
    hi = tone(2*hz, t)
    lo = tone(hz/2, t)
    h = superpose(hi, lo, .5, .5)
    return superpose(a, h, .5, .5)

#-----------------------------------------------------------------------

# Read sound samples from standard input, add harmonics, and play
# the resulting the sound to standard audio.

while not stdio.isEmpty():
    pitch = stdio.readInt()
    duration = stdio.readFloat()
    a = note(pitch, duration)
    stdaudio.playSamples(a)
stdaudio.wait()

#-----------------------------------------------------------------------

# python playthattunedeluxe.py < ascale.txt

# python playthattunedeluxe.py < elise.txt

# python playthattunedeluxe.py < entertainer.txt

# python playthattunedeluxe.py < firstcut.txt

# python playthattunedeluxe.py < freebird.txt

# python playthattunedeluxe.py < looney.txt

# python playthattunedeluxe.py < stairwaytoheaven.txt

