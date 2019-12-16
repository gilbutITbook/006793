#-----------------------------------------------------------------------
# hashst.py
#-----------------------------------------------------------------------

import stdarray

# A SymbolTable object is a collection of key-value pairs. This
# implementation uses a hash table.

class SymbolTable:
    
    #-------------------------------------------------------------------

   # Construct a new SymbolTable object.
    
    def __init__(self, m=1024):
        self._m = m
        self._keys = stdarray.create2D(m, 0)
        self._vals = stdarray.create2D(m, 0)
        
    #-------------------------------------------------------------------

   # Return the value associated with key in self.
    
    def __getitem__(self, key):
        i = hash(key) % self._m    
        for j in range(len(self._keys[i])):
            if self._keys[i][j] == key:
                return self._vals[i][j]
        raise KeyError
    
    #-------------------------------------------------------------------
    
    # Associate key with val in self.
    
    def __setitem__(self, key, val):
        i = hash(key) % self._m
        for j in range(len(self._keys[i])):
            if self._keys[i][j] == key:
                self._vals[i][j] = val
                return
        self._keys[i] += [key]
        self._vals[i] += [val]

    #-------------------------------------------------------------------
    
    # Return True if key is in self, and False otherwise.
    
    def __contains__(self, key):
        i = hash(key) % self._m
        for j in range(len(self._keys[i])):
            if self._keys[i][j] == key:
                return True
        return False

    #-------------------------------------------------------------------

    # Return an iterator for self.
              
    def __iter__(self):
        a = []
        for i in range(self._m):
            a += self._keys[i]
        return iter(a)           

#-----------------------------------------------------------------------

# For testing.

def main():

    import stdio

    # Test the constructor.
    st = SymbolTable()

    # Test __setitem__():
    st['Sedgewick'] = 'Bob'
    st['Wayne'] = 'Kevin'
    st['Dondero'] = 'Bob'

    # Test __getitem__():
    stdio.writeln(st['Sedgewick'])
    stdio.writeln(st['Wayne'])
    stdio.writeln(st['Dondero'])

    # Test __contains__():
    if 'Dondero' in st:
        stdio.writeln('Dondero found')
    else:
        stdio.writeln('Dondero not found')
    if 'Kernighan' in st:
        stdio.writeln('Kernighan found')
    else:
        stdio.writeln('Kernighan not found')

    # Test iteration:
    for key in st:
        stdio.writeln(key + ': ' + st[key])

if __name__ == '__main__':
    main()
  
#-----------------------------------------------------------------------
  
# python hashst.py
# Bob
# Kevin
# Bob
# Dondero found
# Kernighan not found
# Dondero: Bob
# Sedgewick: Bob
# Wayne: Kevin

