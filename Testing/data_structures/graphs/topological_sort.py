from queue import Queue

from adjacency_matrix_graph import AdjacencyMatrixGraph


def topological_sort(graph):
    queue = Queue()
    indegree_map = {}

    for i in range(graph.num_vertices):
        indegree_map[i] = graph.get_in_degree(i)

        # Queue all nodes which have no dependencies i.e.
        # no edges coming in
        if indegree_map[i] == 0:
            queue.put(i)

    sorted_list = []
    while not queue.empty():
        vertex = queue.get()

        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v] = indegree_map[v] - 1

            if indegree_map[v] == 0:
                queue.put(v)

    if len(sorted_list) != graph.num_vertices:
        raise ValueError("This graph has a cycle!")

    print('The topological sort of the graph: ', sorted_list)


gr = AdjacencyMatrixGraph(9, directed=True)
gr.add_edge(0, 1)
gr.add_edge(1, 2)
gr.add_edge(2, 7)
gr.add_edge(2, 4)
gr.add_edge(2, 3)
gr.add_edge(1, 5)
gr.add_edge(5, 6)
gr.add_edge(3, 6)
gr.add_edge(3, 4)
gr.add_edge(6, 8)

topological_sort(gr)
