# Graphs
# Each node may point to another
# Each edge could be directed(one way streets) or undirected(two way streets)
from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = dict()

    def get_vertex(self, vert_name):
        return self.vertices[vert_name]

    def add_vertex(self, vertex):
        # type checks vertex to add - checks if doesnt already exist in dict
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vert1, vert2):
        # checks if vertices are in graph - an edge must have two vertices
        if vert1 in self.vertices and vert2 in self.vertices:
            # loops through existing vertices
            for k, v in self.vertices.items():
                if k == vert1:
                    v.add_neighbor(vert2)
                if k == vert2:
                    v.add_neighbor(vert1)
            return True
        else:
            return False

    def fill_graph(self):
        for i in range(ord('A'), ord('K')):
            self.add_vertex(Vertex(chr(i)))

        edges = ['AB', 'BF', 'CG', 'DE', 'DH','EH', 'FG', 'FJ', 'GJ', 'HI']
        for edge in edges:
            self.add_edge(edge[:1], edge[1:])
        print("\n** Graph initialized ** \nOf type dictionary with keys as vertex name and value as vertex class/type - contains char A-J \n")

    def print_graph(self):
        for key in sorted(list(self.vertices)):
            # prints DFS Mapping
            if self.vertices[key].discovery != 0:
                print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].discovery) + ":" + str(self.vertices[key].finish))
            # prints BFS Mapping
            elif self.vertices[key].distance != 99999:
                print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].distance))
            else:
                print(key + str(self.vertices[key].neighbors))
        print("\n")

    # uses queue to process vertices
    def bfs(self, start_vert=None):
        start_vert = self.vertices['A'] if start_vert == None else start_vert
        nei_que = list()
        start_vert.distance = 0
        start_vert.visited = True
        
        # loop through starting points neighbors to create list of neighbors
        for neighbor in start_vert.neighbors:
            # set distance of each neighbor to incremented value
            self.vertices[neighbor].distance = start_vert.distance + 1
            # append neighbor to
            nei_que.append(neighbor)

        # loops through starting points neighbors to look at their neighbors
        while len(nei_que) > 0:
            # gets key of next vertex in nei_que
            start_vert_next_neighbor = nei_que.pop(0)
            # uses name to extract node
            start_vert_next_node = self.vertices[start_vert_next_neighbor]
            # visits node
            start_vert_next_node.visited = True

            # loops through start node neighbors to look at their neighbors
            for neighbor in start_vert_next_node.neighbors:
                # gets full node of neighbor using key
                next_neighbor_node = self.vertices[neighbor]
                if not next_neighbor_node.visited:
                  nei_que.append(neighbor)
                  if next_neighbor_node.distance > start_vert_next_node.distance + 1:
                    next_neighbor_node.distance = start_vert_next_node.distance + 1
    
    # can be done recursivly or iteratively
    def dfs(self, start_vert=None):
        start_vert = self.vertices['A'] if start_vert == None else start_vert
        global time
        time = 1
        self._dfs_recurs(start_vert)
    
    # internal function
    def _dfs_recurs(self, start_vert):
        global time
        start_vert.visited = True
        start_vert.discovery = time
        time += 1
        for neighbor in start_vert.neighbors:
            if not self.vertices[neighbor].visited:
                self._dfs_recurs(self.vertices[neighbor])
        # sets flag to prevent infinite looping
        start_vert.visited = True
        start_vert.finish = time
        time += 1
