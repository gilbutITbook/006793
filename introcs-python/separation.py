#-----------------------------------------------------------------------
# separation.py
#-----------------------------------------------------------------------

import sys
import stdio
from graph import Graph
from pathfinder import PathFinder

# Accept a file name, a delimiter, and a source vertex as command-line
# arguments. Build a graph from the file, assuming that each line of
# the file specified a vertex and a list of vertices connected to that
# vertex, separated by the delimiter. Then repeatedly read a
# destination vertex from standard input, and write the shortest path
# from the source index to the destination index.

ommand-line arguments file, delimiter, and s. The file 
# contains a graph expressed using delimiter Read data from
# file to create a graph
file = sys.argv[1]
delimiter = sys.argv[2]
s = sys.argv[3]

graph = Graph(file, delimiter)
pf = PathFinder(graph, s)

while stdio.hasNextLine():
    t = stdio.readLine()
    if pf.hasPathTo(t):
        distance = pf.distanceTo(t)
        for v in pf.pathTo(t):
            stdio.writeln('   ' + v)
        stdio.writeln('distance: ' + str(distance))

#-----------------------------------------------------------------------

# python separation.py routes.txt " " JFK
# LAX   
#    JFK
#    ORD
#    PHX
#    LAX
# distance: 3
# DFW
#    JFK
#    ORD
#    DFW
# distance: 2

# python separation.py movies.txt "/" "Bacon, Kevin"
# Kidman, Nicole
#    Bacon, Kevin
#    Wild Things (1998)
#    Dillon, Matt (I)
#    To Die For (1995)
#    Kidman, Nicole
# distance: 4
# Hanks, Tom
#    Bacon, Kevin
#    Apollo 13 (1995)
#    Hanks, Tom
# distance: 2

