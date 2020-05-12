# Breadth First Search
# Goes wide across a given vertecies neighbors before going deep into the graph

from Vertex import Vertex
from Graph import Graph

g = Graph()
g.fill_graph()

# args: Graph, char, char
# returns: boolean  
def hasPathBFS(graph, source, destination):
    
    next_to_visit = list() # list of neighbors to search per level
    visited_set = set() # unique non-repeating values
    
    # inits first vert to be processed
    next_to_visit.append(source)

    # loops while there are verts to visit
    while next_to_visit:
        # remove vertex at index 0 or head of list
        cur_vert_name = next_to_visit.pop(0)
        # checks if source and cur_vert_name are equal
        if cur_vert_name == destination:
            return True
        # checks cur_vert_name has been visited
        if cur_vert_name in visited_set:
            continue
        # adds cur_vert_name to visited vertecies
        visited_set.add(cur_vert_name)
        # gets Vertex class/type to access neighbors property
        cur_vert = g.get_vertex(cur_vert_name)
        for neighbor in cur_vert.neighbors:
            next_to_visit.append(neighbor)

    return False

# SYS OUT
g.print_graph()

vert_1 = 'A'
vert_2 = 'B'
print(vert_1 + " has path to " + vert_2 + "?")
print(hasPathBFS(g, vert_1, vert_2))

vert_1 = 'A'
vert_2 = 'I'
print(vert_1 + " has path to " + vert_2 + "?")
print(hasPathBFS(g, vert_1, vert_2))
