from lab2.dimacs import *
from lab2.Graph import *
from collections import deque


def bfs(graph, starting_v, end_v):
    print('### BFS ####')
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
                print(edge)
                visited_v[edge.end_v] = 1
                edge_to_parent[edge.end_v] = edge
        visited_v[v] = 2
    print('### END BFS ###')

    if visited_v[end_v] == 2:
        graph.update(edge_to_parent, end_v)
        return True

    return False


(V, L) = loadDirectedWeightedGraph("simple")
graph = Graph(V)
residual_graph = Graph(V)

for (start_v, end_v, flow) in L:
    graph.add_edge(flow, start_v, end_v)
    residual_graph.add_edge(flow, start_v, end_v)
    residual_graph.add_edge(0, end_v, start_v)

print('###################')

for edge_list in residual_graph.vertices_list:
    for edge in edge_list:
        print(edge)

print('###################')

bfs(residual_graph, 1, V)

for edge_list in residual_graph.vertices_list:
    for edge in edge_list:
        print(edge)
