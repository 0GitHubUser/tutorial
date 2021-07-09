class Vert:

    def __init__(self, n):
        self.name = n
        self.neighbours = list()

    def add_neighbours(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()
    

class G:

    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vert) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbours(v)
                if key == v:
                    value.add_neighbours(u)
            return True
        else:
            return False


v = Vert('A')
v.add_neighbours('B')
v.add_neighbours('C')
v.add_neighbours('D')

g = G()
g.add_vertex(v)
g.add_edge('C', 'D')

g.print_graph(v)
