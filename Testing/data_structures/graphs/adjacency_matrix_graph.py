import numpy as np

from data_structures.graphs.base_graph import Graph


"""
Represents a graph as an adjacency matrix. A cell in the matrix has
a value when there exists an edge between the vertex represented by
the row and column numbers.
Weighted graphs can hold values > 1 in the matrix cells
A value of 0 in the cell indicates that there is no edge
"""


class AdjacencyMatrixGraph(Graph):

    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)

        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')

        if weight < 1:
            raise ValueError('An edge cannot have weight < 1')

        self.matrix[v1][v2] = weight
        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError('Cannot access vertex %d' % v)

        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_in_degree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f'Cannot access vertex {v}')

        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]


# Test the Graph methods

g = AdjacencyMatrixGraph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

g.display()
