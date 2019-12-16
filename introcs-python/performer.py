#-----------------------------------------------------------------------
# performer.py
#-----------------------------------------------------------------------

import sys
import stdio
import smallworld
from graph import Graph
from instream import InStream

# Accept the name of a movie-cast file and a delimiter as command-line
# arguments and create the associated performer-performer graph. Write
# to standard output the number of vertices, the average degree, 
# the average path length, and the clustering coefficient of the graph.
# Assume that the performer-performer graph is connected so that the
# average page length is defined.

file      = sys.argv[1]
delimiter = sys.argv[2]

graph = Graph()
instream = InStream(file)
while instream.hasNextLine():
    line = instream.readLine()
    names = line.split(delimiter)
    for i in range(1, len(names)):
        for j in range(i+1, len(names)):
            graph.addEdge(names[i], names[j])

degree  = smallworld.averageDegree(graph)
length  = smallworld.averagePathLength(graph)
cluster = smallworld.clusteringCoefficient(graph)

stdio.writef('number of vertices     = %d\n', graph.countV())
stdio.writef('average degree         = %7.3f\n', degree)
stdio.writef('average path length    = %7.3f\n', length)
stdio.writef('clustering coefficient = %7.3f\n', cluster)

#-----------------------------------------------------------------------

# cat tinymovies.txt
# Movie 1/Actor A/Actor B/Actor H
# Movie 2/Actor B/Actor C
# Movie 3/Actor A/Actor C/Actor G

# python performer.py tinymovies.txt "/"
# number of vertices     = 5
# average degree         =   2.800
# average path length    =   1.300
# clustering coefficient =   0.767

# python performer.py moviesg.txt "/"
# number of vertices     = 19044
# average degree         = 148.688
# average path length    =   3.494
# clustering coefficient =   0.911

