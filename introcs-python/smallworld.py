#-----------------------------------------------------------------------
# smallworld.py
#-----------------------------------------------------------------------

import sys
import stdio
import instream
from graph import Graph
from pathfinder import PathFinder

#-----------------------------------------------------------------------

# Return the average degree of graph.

def averageDegree(graph):
    return 2.0 * graph.countE() / graph.countV()

#-----------------------------------------------------------------------

# Return the average path length of graph.

def averagePathLength(graph):
    total = 0
    for v in graph.vertices():
        pf = PathFinder(graph, v)
        for w in graph.vertices():
            total += pf.distanceTo(w)
    return 1.0 * total / (graph.countV() * (graph.countV() - 1))

#-----------------------------------------------------------------------

# Return the clustering coefficient of graph.

def clusteringCoefficient(graph):
    total = 0
    for v in graph.vertices():
        possible = graph.degree(v) * (graph.degree(v) - 1)
        actual = 0
        for u in graph.adjacentTo(v):
            for w in graph.adjacentTo(v):
                if graph.hasEdge(u, w):
                    actual += 1
        if possible > 0:
            total += 1.0 * actual / possible
    return total / graph.countV()

#-----------------------------------------------------------------------

# Test client.

def main():

    graphFile = sys.argv[1]
    delimiter = sys.argv[2]
    
    graph = Graph(graphFile, delimiter)
    
    vertexCount = graph.countV()
    edgeCount = graph.countE()
    stdio.writef('%d vertices, %d edges\n', vertexCount, edgeCount)
    
    avgDegree = averageDegree(graph)
    stdio.writef('average degree         = %7.3f\n', avgDegree)
    
    avgPathLength = averagePathLength(graph)
    stdio.writef('average path length    = %7.3f\n', avgPathLength)

    clusteringCoef = clusteringCoefficient(graph)
    stdio.writef('clustering coefficient = %7.3f\n', clusteringCoef)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python smallworld.py tinygraph.txt " "
# 5 vertices, 7 edges
# average degree         =   2.800
# average degree         =   1.300
# clustering coefficient =   0.767

