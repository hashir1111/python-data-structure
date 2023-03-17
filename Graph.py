class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def get_adjacent_vertices(self, v):
        if v in self.adj_list:
            return self.adj_list[v]
        else:
            return None

    def get_vertices(self):
        return list(self.adj_list.keys())
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')

print(g.get_vertices())  
print(g.get_adjacent_vertices('B')) 
