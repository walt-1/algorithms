# Vertex class to represent graph nodes
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.distance = 99999
        self.visited = False
        self.discovery = 0
        self.finish = 0

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            # store neighbors in sorted list
            self.neighbors.sort()
