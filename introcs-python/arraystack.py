#-----------------------------------------------------------------------
# arraystack.py
#-----------------------------------------------------------------------

import stdio

# A Stack object is a last-in-first-out collection.

class Stack:

    #-------------------------------------------------------------------

    # Construct an empty Stack object.

    def __init__(self):
        self._a = []  # Items

    #-------------------------------------------------------------------

    # Return True if self is empty, and False otherwise.

    def isEmpty(self):
        return len(self._a) == 0

    #-------------------------------------------------------------------

    # Push object item onto the top of self.

    def push(self, item):
        self._a += [item]

    #-------------------------------------------------------------------

    # Pop the top object from self and return it.

    def pop(self):
        return self._a.pop()

    #-------------------------------------------------------------------

    # Return a string representation self.

    def __str__(self):
        s = ''
        for item in self._a:
            s = str(item) + ' ' + s
        #for item in reversed(self._a):
        #    s += str(item) + ' '
        return s

#-----------------------------------------------------------------------

# Test the Stack class by reading strings from standard input and
# pushing or popping as indicated. A minus sign indicates pop (and
# write to standard output), and any other string indicates push.

def main():
    stack = Stack()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            stack.push(item)
        else:
            stdio.write(stack.pop() + ' ')
    stdio.writeln()

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# more tobe.txt
# to be or not to - be - - that - - - is

# python3.4 arraystack.py < tobe.txt 
# to be not that or be

