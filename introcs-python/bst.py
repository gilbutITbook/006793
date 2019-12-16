#-----------------------------------------------------------------------
# bst.py
#-----------------------------------------------------------------------

# An OrderedSymbolTable object is a collection of key-value pairs that
# is kept in order by key. This implementation uses a binary search
# tree.

class OrderedSymbolTable:

    #-------------------------------------------------------------------

    # Construct a new OrderedSymbolTable object.

    def __init__(self):
        self._root = None  # Reference to root _Node object

    #-------------------------------------------------------------------

    # Search the subtree of self whose root is x for a _Node object
    # with the given key.  If found, return that _Node object's value;
    # otherwise raise a KeyError.

    def _get(self, x, key):
        if x is None:
            raise KeyError
        if key < x.key:
            return self._get(x.left, key)
        elif x.key < key:
            return self._get(x.right, key)
        else:
            return x.val

   # Return the value associated with key in self.

    def __getitem__(self, key):
        return self._get(self._root, key)

    #-------------------------------------------------------------------

    # x is the root of a subtree self.  If a _Node object with
    # the given key exists in that subtree, then set its
    # value to val.  Otherwise insert a new _Node object consisting
    # of the given key and val into the subtree.  Return the root of
    # the resulting subtree.

    def _set(self, x, key, val):
        if x is None:
            return _Node(key, val)
        if key < x.key:
            x.left = self._set(x.left, key, val)
        elif x.key < key:
            x.right = self._set(x.right, key, val)
        else:
            x.val = val
        return x

    # Associate key with val in self.

    def __setitem__(self, key, val):
        self._root = self._set(self._root, key, val)

    #-------------------------------------------------------------------

    # Search the subtree of self whose root is x for a _Node object
    # with the given key.  If found, return True; otherwise return
    # False.

    def _contains(self, x, key):
        if x is None:
            return False
        if key < x.key:
            return self._contains(x.left, key)
        if x.key < key:
            return self._contains(x.right, key)
        return True

    # Return True if key is in self, and False otherwise.

    def __contains__(self, key):
        return self._contains(self._root, key)

    #-------------------------------------------------------------------

    # Populate list a with all keys in the subtree of self whose
    # root is x.

    def _inorder(self, x, a):
        if x is None:
            return
        self._inorder(x.left, a)
        a += [x.key]
        self._inorder(x.right, a)

    # Return an iterator for SymTable object self.

    def __iter__(self):
        a = []
        self._inorder(self._root, a)
        return iter(a)

#-----------------------------------------------------------------------

# A _Node object references a key, a value, and left and right
# children _Node objects.  An OrderedSymTable object is composed of
# _Node objects.

class _Node:
    def __init__(self, key, val):
        self.key = key    # Reference to key
        self.val = val    # Reference to value
        self.left = None  # Reference to left child _Node object
        self.right = None # Reference to right child _Node object

#-----------------------------------------------------------------------

# For testing.

def main():

    import stdio

    # Test the constructor.
    st = OrderedSymbolTable()

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

# python bst.py
# Bob
# Kevin
# Bob
# Dondero found
# Kernighan not found
# Dondero: Bob
# Sedgewick: Bob
# Wayne: Kevin

