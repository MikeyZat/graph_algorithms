from lab2.dimacs import *
from lab2.Graph import *
from collections import deque
import time


def print_graph(graph):
    for edge_list in graph.vertices_list:
        for edge in edge_list:
            print(edge)


def bfs(graph, starting_v):
    queue = deque()
    visited_v = [0] * graph.size
    edge_to_parent = [None] * graph.size
    queue.append(starting_v)
    visited_v[starting_v] = 1
    while queue:
        v = queue.popleft()
        edge_list = graph.vertices_list[v]
        for edge in edge_list:
            if visited_v[edge.end_v] == 0 and edge.capacity > 0:
                queue.append(edge.end_v)
                visited_v[edge.end_v] = 1
                edge_to_parent[edge.end_v] = (edge, edge.correspondive_edge)
        visited_v[v] = 2
    return visited_v, edge_to_parent


def find_path_and_update(graph, starting_v, end_v):
    visited_v, edge_to_parent = bfs(graph, starting_v)
    if visited_v[end_v] == 2:
        graph.update(edge_to_parent, end_v)
        return True

    return False


(V, L) = loadDirectedWeightedGraph("graphs/grid100x100")
graph = Graph(V)
residual_graph = Graph(V, True)

for (start_v, end_v, capacity) in L:
    graph.add_edge(capacity, start_v, end_v)
    residual_graph.add_edge(capacity, start_v, end_v)

# print('###################')
#
# print('Graph:')
# print_graph(graph)
# print('Residual graph created:')
# print_graph(residual_graph)

print('###################')
start = time.time()
b = find_path_and_update(residual_graph, 1, V)
while b:
    b = find_path_and_update(residual_graph, 1, V)
stop = time.time() - start
print(residual_graph.flow)
print(stop)