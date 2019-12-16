#-----------------------------------------------------------------------
# timeops.py
#-----------------------------------------------------------------------

import stdio
import stopwatch
import sys
import math
import random

#-----------------------------------------------------------------------

# Return 0. (This is a nonsensical function used only for timing.

def f(i, j):
    return 0

#-----------------------------------------------------------------------

# Accept integer command-line argument n. Determine the time required
# to perform n^2 integer additions, integer subtractions, integer
# divisions, integer remainders integer comparisons, floating point
# additions, floating point subtractions, floating point
# multiplications, fn and floating point divisions. Write the times
# to standard output.

# Beware that the compiler may optimize away some code.

def main():

    n = int(sys.argv[1])

    stdio.writeln('Nanoseconds per operation')

    #-------------------------------------------------------------------
    # Empty loop
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(n):
            pass
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Empty loop')

    #-------------------------------------------------------------------
    # Integer addition
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = i + j
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Integer addition')

    #-------------------------------------------------------------------
    # Integer subtraction
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = i - j
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Integer subtraction')

    #-------------------------------------------------------------------
    # Integer multiplication
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = i * j
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Integer multiplication')

    #-------------------------------------------------------------------
    # Integer division
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = i // j
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Integer division')

    #-------------------------------------------------------------------
    # Integer remainder
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = i % j
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Integer remainder')

    #-------------------------------------------------------------------
    # Comparison
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            b = (i < j)
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Comparison')

    #-------------------------------------------------------------------
    # Floating point addition
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = float(i) + float(j)
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Floating point addition')

    #-------------------------------------------------------------------
    # Floating point subtraction
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = float(i) - float(j)
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Floating point subtraction')

    #-------------------------------------------------------------------
    # Floating point multiplication
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = float(i) * float(j)
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Floating point multiplication')

    #-------------------------------------------------------------------
    # Floating point division
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = float(i) / float(j)
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Floating point division')

    #-------------------------------------------------------------------
    # Function call
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = f(i, j)
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Function call')

    #-------------------------------------------------------------------
    # math.sin
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n//10+1):
        for j in range(1, n+1):
            k = math.sin(i + j)
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n) * 10.0
    stdio.writef('%7.1f: %s\n', freq, 'math.sin')

    #-------------------------------------------------------------------
    # math.atan2
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n//10+1):
        for j in range(1, n+1):
            k = math.atan2(i, j)
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n) * 10.0
    stdio.writef('%7.1f: %s\n', freq, 'math.atan2')

    #-------------------------------------------------------------------
    # random.random
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n//10+1):
        for j in range(1, n+1):
            k = random.random()
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n) * 10.0
    stdio.writef('%7.1f: %s\n', freq, 'random.random')

    #-------------------------------------------------------------------
    # Integer addition
    #-------------------------------------------------------------------

    timer = stopwatch.Stopwatch()
    for i in range(1, n+1):
        for j in range(1, n+1):
            k = i + j
    elapsed = timer.elapsedTime()
    freq = 1.0E9 * elapsed / float(n) / float(n)
    stdio.writef('%7.1f: %s\n', freq, 'Integer addition again')

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# Example executions:

# python timeops.py 1000
# python timeops.py 10000

