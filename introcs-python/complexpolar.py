#-----------------------------------------------------------------------
# complex.py
#-----------------------------------------------------------------------

import stdio
import math

# A Complex object is a complex number.

# A Complex object is immutable.  So once you create and initialize
# a Complex object, you cannot change it.

class Complex:

    # Construct a new Complex object with real part real and imaginary
    # part imag. real defaults to 0.0. imag also defaults to 0.0.
    def __init__(self, re=0.0, im=0.0):
        self._r = math.sqrt(re*re + im*im)
        self._theta = math.atan2(im, re)

    # Return the real part of Complex object self.
    def re(self):
        return self._r * math.cos(self._theta)

    # Return the imaginary part of Complex object self.
    def im(self):
        return self._r * math.sin(self._theta)

    # Return the conjugate of Complex object self.
    def conjugate(self):
        return Complex(self.re(), -self.im())

    # Return a new Complex object which is the sum of Complex objects
    # self and other.
    def __add__(self, other):
        re = self.re() + other.re()
        im = self.im() + other.im()
        return Complex(re, im)

    # Return a new Complex object which is the product of Complex
    # objects self and other.
    def __mul__(self, other):
        c = Complex(0, 0)
        c._r = self._r * other._r
        c._theta = self._theta + other._theta
        return c

    # Return True if Complex objects self and other are equal, and
    # False otherwise.
    # def __eq__(self, other):
    #     return (self._r == other._r) and \
    #            (self._theta == other._theta)

    # Return True if Complex objects self and other are unequal, and
    # False otherwise.
    # def __ne__(self, other):
    #     return not self.__eq__(other)

    # Return the absolute value of Complex object self.
    def __abs__(self):
        return self._r

    # Return a string representation of Complex object self.
    def __str__(self):
        return str(self.re()) + ' + ' + str(self.im()) + 'i'

#-----------------------------------------------------------------------

# For testing.
# Create and use some Complex objects.

def main():

    z0 = Complex(1.0, 1.0)
    z = z0
    z = z * z + z0
    z = z * z + z0
    stdio.writeln(z)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python complexpolar.py
# -7.000000000000002 + 7.000000000000003i

