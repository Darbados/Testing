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

    def get_in_degree(self, v):
        raise NotImplementedError()

    def get_edge_weight(self, v1, v2):
        raise NotImplementedError()

    def display(self):
        self.display_vertex_properties()

        print('#############################')
        print('        Display Graph        ')
        for v1 in range(self.num_vertices):
            for adjacent_vertex in self.get_adjacent_vertices(v1):
                print(f'{v1} ---> {adjacent_vertex}')
        print('      End Display Graph      ')
        print('#############################')

    def display_vertex_properties(self):
        print('#############################')
        print('  Display vertex relations   ')
        print('#############################')

        print('#############################')
        for vertex in range(self.num_vertices):
            print(f'Vertex {vertex} adjacent vertices: {self.get_adjacent_vertices(vertex)}')
        print('#############################')

        print('#############################')
        for vertex in range(self.num_vertices):
            print(f'Vertex {vertex} in degree: {self.get_in_degree(vertex)}')
        print('#############################')

        print('#############################')
        for vertex in range(self.num_vertices):
            for adjacent_vertex in self.get_adjacent_vertices(vertex):
                print('Vertex {vertex} edge weight to {adjacent_vertex}: {edge_weight}'.format(
                    vertex=vertex,
                    adjacent_vertex=adjacent_vertex,
                    edge_weight=self.get_edge_weight(vertex, adjacent_vertex),
                ))
        print('#############################')


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
