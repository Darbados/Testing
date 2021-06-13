"""
The base class representation of a Graph with all the interface
methods
"""


class Graph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    def add_edge(self, v1, v2, weight):
        raise NotImplementedError()

    def get_adjacent_vertices(self, v):
        raise NotImplementedError()

    def get_indegree(self, v):
        raise NotImplementedError()

    def get_edge_weight(self, v1, v2):
        raise NotImplementedError()

    def display(self):
        raise NotImplementedError()


"""
A single node in a graph represented by an adjacency set. Every node
has a vertex id
Each node is associated with a set of adjacent vertices
"""


class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError(f'The vertex {v} cannot be adjacent to itself')

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)
