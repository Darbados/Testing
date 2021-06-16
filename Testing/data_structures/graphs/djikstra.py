from data_structures.graphs.adjacency_matrix_graph import AdjacencyMatrixGraph
from data_structures.graphs.adjance_set_graph import AdjacencySetGraph
from data_structures.graphs.priority_dict import priority_dict


def build_distance_table(graph, start):
    # A dictionary mapping from the vertex number to a tuple of
    # (distance from source, last vertex on path from source)
    distance_table = {}

    for vertex in range(graph.num_vertices):
        # Store the vertex's distance for the source and the preceding vertex
        distance_table[vertex] = (None, None)

    distance_table[start] = (0, start)

    # Holds mapping of vertex id to distance from source
    # Access the highest priority (lowest distance) item
    # first
    priority_queue = priority_dict()
    priority_queue[start] = 0

    while len(priority_queue.keys()):
        current_vertex = priority_queue.pop_smallest()
        current_distance = distance_table[current_vertex][0]

        for adjacent_vertex in graph.get_adjacent_vertices(current_vertex):
            distance = current_distance + graph.get_edge_weight(current_vertex, adjacent_vertex)
            adjacent_distance = distance_table[adjacent_vertex][0]

            # If there is a currently recorded distance from the source and this is
            # greater than the distance of the new path found, update the current
            # distance from the source in the distance table
            if adjacent_distance is None or adjacent_distance > distance:
                distance_table[adjacent_vertex] = (distance, current_vertex)
                priority_queue[adjacent_vertex] = distance

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


# g = AdjacencySetGraph(8, directed=False)
g = AdjacencyMatrixGraph(9, directed=False)
g.add_edge(0, 1, weight=3)
g.add_edge(0, 3, weight=2)
g.add_edge(0, 8, weight=4)
g.add_edge(1, 7, weight=4)
g.add_edge(7, 2, weight=2)
g.add_edge(2, 3, weight=6)
g.add_edge(2, 5, weight=1)
g.add_edge(5, 6, weight=8)
g.add_edge(3, 4, weight=1)
g.add_edge(4, 8, weight=8)

# g.display()

shortest_path(g, 0, 6)
# shortest_path(g, 4, 7)
# shortest_path(g, 7, 0)
