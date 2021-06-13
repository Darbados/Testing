from data_structures.graphs.base_graph import Graph, Node


"""
Represents a graph as an adjacency set. A graph is a list of Nodes
and each Node has a set of adjacent vertices. 
This graph in this current form cannot be used to represent
weighted edges only unweighted edges can be represented
"""


class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')

        if weight != 1:
            raise ValueError('An adjacency set cannot represent edge weights >1')

        self.vertex_list[v1].add_edge(v2)
        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')

        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError('Cannot access vertex %d' % v)

        indegree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


g = AdjacencySetGraph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))

for i in range(4):
    print("Indegree: ", i, g.get_indegree(i))

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

g.display()

