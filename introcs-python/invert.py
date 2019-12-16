#-----------------------------------------------------------------------
# invert.py
#-----------------------------------------------------------------------

import sys
import stdio
from graph import Graph

# Accept a string file name and a delimiter as command-line arguments.
# Build a graph from the file. Repeatedly read a vertex name from
# standard input and write the neighbors of that vertex.

file = sys.argv[1]
delimiter = sys.argv[2]
graph = Graph(file, delimiter)
while stdio.hasNextLine():
    v = stdio.readLine()
    if graph.hasVertex(v):
        for w in graph.adjacentTo(v):
            stdio.writeln('  ' + w)
            
#-----------------------------------------------------------------------

# python invert.py tinygraph.txt " "
# C
#   B
#   G
#   A
# A
#   B
#   C
#   G
#   H

# python invert.py movies.txt "/"
# Da Vinci Code, The (2006)
#   Rees, Norman Campbell
#   Chicot, Etienne
#   Gabel, Seth
#   Barker, Tom (VI)
#   Davies, Rita
#   Robb, Andy
#   Berteloot, Jean-Yves
#   Grossi, Joe
#   Molina, Alfred (I)
#   John-Leopoldie, Roland
#   Aubert, Yves
#   Hanks, Tom
#   Emanuel, Crisian
#   Herbert, Paul (IV)
#   Maskell, Tina
#   Black, Rachael
#   Sciarappa, Fausto Maria
#   Vernazza, Mario
#   De Guillebon, Xavier
#   L'Abidine, Dhaffer
#   Carnelutti, Francesco
#   Bertenshaw, Michael
#   Pedrero, Peter
#   Bettany, Paul
#   Roper, Mark (II)
#   Picknett, Lynn
#   McKellen, Ian
#   Descanvelle, Tonio
#   Mitchell, Hugh (I)
#   Parker, Daz
#   Wildor, Sarah
#   Norton, Michael (II)
#   Huillet, Aewia
#   Podalydes, Denis
#   Lillis, Andre
#   Drummond, Dez
#   Reno, Jean (I)
#   Clark, Andrew (V)
#   Fosh, Christopher
#   Bark-Jones, David
#   Carter, Clive
#   Butler, Matthew (VI)
#   Mancuso, Sam
#   Natanson, Agathe
#   Zaza, Shane
#   Guy-Bremond, Lionel
#   Menou, Roland
#   Audollent, Marie-Francoise
#   Tautou, Audrey
#   Doidge-Hill, Daisy
#   Little, Brock
#   McEwan, Maggie
#   Bertrand, David (I)
#   Kelleher, Lilli Ella
#   Prince, Clive
#   Mazureck, Garance
#   Graham, Charlotte (IV)
#   Wilson, Serretta
#   Marielle, Jean-Pierre
#   Rembauville-Nicolle, Eglantine
#   Taylor, Harry (I)
#   Klein, Arnaud
#   Prochnow, Jurgen
#   Tondowski, Dan
#   Saracino, David
# Bacon, Kevin
#   Novocaine (2001)
#   My Dog Skip (2000)
#   Trapped (2002)
#   River Wild, The (1994)
#   Wild Things (1998)
#   Mystic River (2003)
#   Footloose (1984)
#   He Said, She Said (1991)
#   Apollo 13 (1995)
#   She's Having a Baby (1988)
#   Friday the 13th (1980)
#   Murder in the First (1995)
#   Few Good Men, A (1992)
#   Where the Truth Lies (2005)
#   Beauty Shop (2005)
#   Sleepers (1996)
#   Hollow Man (2000)
#   Animal House (1978)
#   In the Cut (2003)
#   Picture Perfect (1997)
#   Diner (1982)
#   Stir of Echoes (1999)
#   JFK (1991)
#   Planes, Trains & Automobiles (1987)
#   Woodsman, The (2004)
#   Flatliners (1990)
#   Tremors (1990)

