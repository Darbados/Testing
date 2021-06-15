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

        # if weight != 1:
        #     raise ValueError('An adjacency set cannot represent edge weights >1')

        self.vertex_list[v1].add_edge(v2, weight)
        if not self.directed:
            self.vertex_list[v2].add_edge(v1, weight)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')

        return self.vertex_list[v].get_adjacent_vertices()

    def get_in_degree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError('Cannot access vertex %d' % v)

        in_degree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                in_degree = in_degree + 1

        return in_degree

    def get_edge_weight(self, v1, v2):
        for adjacent_vertex, weight in self.vertex_list[v1].adjacency_set:
            if adjacent_vertex == v2:
                return weight
        return 0


set_graph = AdjacencySetGraph(9, directed=True)
set_graph.add_edge(1, 2)
set_graph.add_edge(1, 3)
set_graph.add_edge(1, 4)
set_graph.add_edge(2, 3)
set_graph.add_edge(2, 6)
set_graph.add_edge(5, 4)

set_graph.display()

