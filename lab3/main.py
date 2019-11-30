from lab2.dimacs import *
from lab2.Graph import Graph as Graph_1
from lab3.Graph import Graph as Graph_2
from lab2.main import find_path_and_update
from queue import PriorityQueue


def ford_fulkerson(graph_name):
    (V, L) = loadDirectedWeightedGraph(graph_name)
    residual_graph = Graph_1(V, True)
    edge_set = set()
    for (start_v, end_v, capacity) in L:
        if (start_v, end_v) not in edge_set:
            edge_set.add((start_v, end_v))
            residual_graph.add_edge(capacity, start_v, end_v)
        if (end_v, start_v) not in edge_set:
            edge_set.add((end_v, start_v))
            residual_graph.add_edge(capacity, end_v, start_v)

    print('###################')
    b = find_path_and_update(residual_graph, 1, V)
    while b:
        b = find_path_and_update(residual_graph, 1, V)
    return residual_graph.flow


def print_graph(graph):
    for index, vertice in enumerate(graph.vertices_list):
        print('vertice ' + str(index) + ' with edges:\n' + str(vertice))


def minimum_cut_phase(graph):
    # print_graph(graph)
    result = 0
    starting_index = 1
    previous_vertex = last_vertex = starting_index
    # currently available vertices (these already merged don't count)
    V = set([vertex for vertex in graph.vertices_list if not vertex.merged and vertex.index != 0])
    # Set to which we will add vertices
    S = [False for _ in range(len(graph.vertices_list) + 1)]
    # current distance (used for priority queue)
    dist = [0 for _ in range(len(graph.vertices_list) + 1)]
    # Make starting vertex visited
    V.remove(graph.vertices_list[starting_index])
    S[starting_index] = True

    Q = PriorityQueue()

    while len(V) > 0:
        previous_vertex = last_vertex

        for vertex_index, value in graph.vertices_list[previous_vertex].edges.items():
            if not S[vertex_index]:
                dist[vertex_index] += value
                Q.put((-dist[vertex_index], vertex_index))
        result, last_vertex = Q.get()
        if not S[last_vertex]:
            S[last_vertex] = True
            V.remove(graph.vertices_list[last_vertex])

    graph.merge_vertices(previous_vertex, last_vertex)
    return -result


def stoer_wagner(graph_name):
    (V, L) = loadDirectedWeightedGraph(graph_name)
    graph = Graph_2(V)
    for (start_v, end_v, capacity) in L:
        graph.add_edge(start_v, end_v, capacity)

    result = minimum_cut_phase(graph)
    while graph.size != 1:
        result = min(result, minimum_cut_phase(graph))
    return result


print(stoer_wagner('graphs/rand100_500'))
