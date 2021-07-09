class Vrtx:


    def __init__(self, n):
        self.name = n
        self.data = {}
        self.data['neighbours'] = list()
        self.data['edges'] = list()

    def add_neighbours(self, v):
        if v not in self.data['neighbours']:
            self.data['neighbours'].append(v)
            self.data['neighbours'].sort()

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertices(self, vrt):
        if isinstance(vrt, Vrtx) and vrt.name not in self.vertices:
            self.vertices[vrt.name] = vrt.data['neighbours']

    def add_edge(self, vrt, u, v):
        if isinstance(vrt, Vrtx) and vrt.name in self.vertices and vrt.name in (u, v):
            vrt.data['edges'].append((u, v))

    def print_graph(self, vrt):
        print(vrt.data)
        print(self.vertices)



v = Vrtx('A')
v.add_neighbours('B')
v.add_neighbours('C')
v.add_neighbours('D')

g = Graph()
g.add_vertices(v)
g.add_edge(v, 'C', 'D')
g.add_edge(v, 'A', 'D')
g.add_edge(v, 'A', 'B')

g.print_graph(v)


            