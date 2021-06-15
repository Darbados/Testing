from queue import Queue

from data_structures.graphs.adjacency_matrix_graph import AdjacencyMatrixGraph


def build_distance_table(graph, start):
    distance_table = {}

    for vertex in range(graph.num_vertices):
        distance_table[vertex] = (None, None)

    distance_table[start] = (0, start)

    queue = Queue()
    queue.put(start)

    while not queue.empty():
        current_vertex = queue.get()
        current_distance = distance_table[current_vertex][0]

        for adjacent_vertex in graph.get_adjacent_vertices(current_vertex):
            if distance_table[adjacent_vertex][0] is None:
                distance_table[adjacent_vertex] = (current_distance + 1, current_vertex)

                if len(graph.get_adjacent_vertices(adjacent_vertex)):
                    queue.put(adjacent_vertex)

    return distance_table


def shortest_path(graph, start, destination):
    distance_table = build_distance_table(graph, start)

    path = [destination]
    previous_vertex = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not start:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]

    if previous_vertex is None:
        print(f'There is not path from vertex {start} to vertex {destination}')
    else:
        path = [start] + path
        print(f'The path from vertex {start} to vertex {destination} is {path}')


gr = AdjacencyMatrixGraph(8, directed=True)
gr.add_edge(0, 1)
gr.add_edge(1, 2)
gr.add_edge(1, 3)
gr.add_edge(2, 3)
gr.add_edge(1, 4)
gr.add_edge(3, 5)
gr.add_edge(5, 4)
gr.add_edge(3, 6)
gr.add_edge(6, 7)
gr.add_edge(0, 7)


print(build_distance_table(gr, 0))
shortest_path(gr, 0, 5)
shortest_path(gr, 0, 6)
shortest_path(gr, 7, 4)

