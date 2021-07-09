
global index 
index = 0
class MVrtx:

    def __init__(self, n):
        self.name = n
        self.neighbours = list()

    def add_neighbours(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)

class MGraph:

    def __init__(self):
        self.vertices = {}
        self.matrix = []

        
    def add_vertex(self, vrt):
        global index
        if isinstance(vrt, MVrtx) and vrt.name not in self.vertices.keys():
            self.vertices[vrt] = index
            index += 1
            self.matrix.append([])

    def

    def print_vertices(self):
        print(self.vertices)
        print(self.matrix)

g = MGraph()

v1 = MVrtx('A')
v1.add_neighbours('B')
v1.add_neighbours('C')

v2 = MVrtx('B')
v2.add_neighbours('A')
v2.add_neighbours('C')
v2.add_neighbours('F')

v3 = MVrtx('C')
v3.add_neighbours('E')
v3.add_neighbours('D')

v4 = MVrtx('D')
v4.add_neighbours('G')
v4.add_neighbours('C')
v4.add_neighbours('F')

g.add_vertex(v1)
g.add_vertex(v2)
g.add_vertex(v3)
g.add_vertex(v4)


g.print_vertices()