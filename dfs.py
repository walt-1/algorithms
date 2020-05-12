# Breadth First Search
# Goes wide to neighbors before going deep into the graph moving level by level

from Vertex import Vertex
from Graph import Graph

g = Graph()
g.fill_graph()

# exposed function
def hasPathDFS(graph, source, destination):
    # creates start vert
    # creates dest vert
    # creates visited hastable
    # calls helper function to start accumulating 
    start_vert = graph.get_vertex(source)
    dest_vert = graph.get_vertex(destination)
    visited_map = dict()
    return _DFS(graph, start_vert, dest_vert, visited_map)

# helper function
def _DFS(graph, cur_vert, dest_vert, visited_map):
    # region Base Case
    # use key to find item in hash map
    if cur_vert.name in visited_map:
        return False
    # sets vertex to visited
    visited_map[cur_vert.name] = cur_vert
    # checks is base case is satisfied
    if cur_vert == dest_vert:
        return True
    # endregion
     
    # region Recurse
    for neighbor in cur_vert.neighbors:
        next_vert = graph.get_vertex(neighbor)
        if _DFS(graph, next_vert, dest_vert, visited_map):
            return True
    # endregion
    return False

# DFS iteratively
def dfs_iterate(graph, vert):
    next_to_visit = list()  # creat hash set
    seen = dict()           # push first vert onto stack
    
    # inits first vert to be processed
    next_to_visit.append(graph.get_vertex(vert))
    
    # loop while stack has items
    while next_to_visit:
        # init cur node with pop off of stack
        cur = next_to_visit.pop()
        # check if cur in seen hash set - if not, add cur to hash set
        if cur.name not in seen:
            print(cur.name)
            seen[cur.name] = True

        # loop over cur nodes neighbors
        for node in cur.neighbors:
            cur = graph.get_vertex(node)
            # check each node in seen - if not add to stack
            if cur.name not in seen:
                next_to_visit.append(cur)


def dfs_recurse(graph, vert, seen):
    cur = graph.get_vertex(vert)

    # check if cur in seen hash set - if not, add cur to hash set
    if cur.name not in seen:
        print(cur.name)
        seen[cur.name] = True

    # loop over cur nodes neighbors
    for node_name in cur.neighbors:
        if node_name not in seen:
            dfs_recurse(graph, node_name, seen)

# SYS OUT
# g.print_graph()
# vert_1 = 'A'
# vert_2 = 'I'
# print("Is the a path from " + vert_1 + " to " + vert_2 + "?")
# print(hasPathDFS(g, vert_1, vert_2))

# vert_1 = 'A'
# vert_2 = 'B'
# print("Is the a path from " + vert_1 + " to " + vert_2 + "?")
# print(hasPathDFS(g, vert_1, vert_2))

s = dict()
print(dfs_iterate(g, 'A'))
