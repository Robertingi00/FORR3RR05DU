class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
            self.visited = False


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

    def _dfs(self, vertex, visited):
        if(vertex not in visited):
            visited[vertex] = vertex
            print("Vertices",self.vertices[vertex].name)
            print(self.vertices[vertex].neighbors)
            for i in self.vertices[vertex].neighbors:
                self._dfs(i,visited)

    def dfs(self, vertex):
        visited = {}
        self._dfs(vertex,visited)

    def _bfs(self, vertex, visited, q):
        if (vertex not in visited):
            visited[vertex] = vertex
            print("Vertices", self.vertices[vertex].name)
            print(self.vertices[vertex].neighbors)
            if(len(q) > 0):
                q.pop(0)

            for i in self.vertices[vertex].neighbors:
                if(i not in q):
                    q.append(i)

            for i in q:
                    self._bfs(i, visited, q)



    def bfs(self, vertex):
        visited = {}
        q = []
        self._bfs(vertex, visited, q)

g = Graph()

a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.bfs("A")