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
    last_vertex = graph.vertices_list[1]
    S = set(1)
    Q = PriorityQueue()
    while len(S) < graph.size:
        for vertex_index in last_vertex.edges.keys():
            if vertex_index not in S:
                Q.put((-last_vertex.edges[vertex_index], vertex_index))

def stoer_wagner(graph_name):
    (V, L) = loadDirectedWeightedGraph(graph_name)
    graph = Graph_2(V)
    for (start_v, end_v, capacity) in L:
        graph.add_edge(start_v, end_v, capacity)


    minimum_cut_phase(graph)

    # print('###################')
    # b = find_path_and_update(graph, 1, V)
    # while b:
    #     b = find_path_and_update(graph, 1, V)
    # return graph.flow


stoer_wagner('graphs/clique5')
