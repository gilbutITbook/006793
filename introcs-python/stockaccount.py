#-----------------------------------------------------------------------
# stockaccount.py
#-----------------------------------------------------------------------

import sys
import stdio
import stdarray
from instream import InStream
from outstream import OutStream
import stockquote

#-----------------------------------------------------------------------

class StockAccount:

    # Construct self by reading data from the file whose name is
    # fileName.
    def __init__(self, fileName):
        inStream = InStream(fileName)
        self._name = inStream.readLine()      # Customer name
        self._cash = inStream.readFloat()     # Cash balance
        self._stockCount = inStream.readInt() # Number of stocks
        # Stock symbols
        self._stocks = stdarray.create1D(self._stockCount, 0)
        # Share counts
        self._shares = stdarray.create1D(self._stockCount, 0)
        for i in range(self._stockCount):
            self._shares[i] = inStream.readInt()
            self._stocks[i] = inStream.readString()

    # Return the total value in dollars of self.
    def valueOf(self):
        total = self._cash
        for i in range(self._stockCount):
            price = stockquote.priceOf(self._stocks[i])
            amount = self._shares[i]
            total += amount * price
        return total

    # Write to OutStream object outStream the data of self.
    def write(self, outStream):
        outStream.writeln(self._name)
        outStream.writeln(self._cash)
        outStream.writeln(self._stockCount)
        for i in range(self._stockCount):
            outStream.writef('%3d', self._shares[i])
            outStream.write(' ')
            outStream.writeln(self._stocks[i])

    # Write to standard output a detailed report of the stocks and
    # values in self.
    def writeReport(self):
        stdio.writeln(self._name)
        total = self._cash
        for i in range(self._stockCount):
            amount = self._shares[i]
            price = stockquote.priceOf(self._stocks[i])
            total += amount * price
            stdio.writef('%4d  %4s ', amount, self._stocks[i])
            stdio.writef('  %7.2f   %9.2f\n', price, amount * price)
        stdio.writef('%21s %10.2f\n', 'Cash:', self._cash)
        stdio.writef('%21s %10.2f\n', 'Total:', total)

#-----------------------------------------------------------------------

# Accept as a command-line argument the name of a file. Read
# from the file to create a StockAccount object. Write a report to
# standard output.

def main():
    acct = StockAccount(sys.argv[1])
    acct.writeReport()

if __name__ == '__main__':
    import sys
    main()

#-----------------------------------------------------------------------

# more turing.txt
# Turing, Alan
# 10.24
# 4
# 100 ADBE
#  25 GOOG
#  97 IBM
# 250 MSFT

# python stockaccount.py turing.txt
#Turing, Alan
# 100  ADBE     92.17     9217.00
#  25  GOOG    750.26    18756.50
#  97   IBM    138.46    13430.62
# 250  MSFT     53.93    13482.50
#                Cash:      10.24
#               Total:   54896.86

