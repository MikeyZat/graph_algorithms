from lab2.Edge import *


class Graph:
    def __init__(self, size):
        self.vertices_list = [[] for _ in range(size + 1)]
        self.size = size + 1
        self.flow = 0

    def add_verticle(self, edge_list):
        self.vertices_list.append(
            edge_list
        )

    def add_edge(self, capacity, start_v, end_v):
        self.vertices_list[start_v].append(
            Edge(capacity, start_v, end_v)
        )

    def update(self, edge_to_parent, end_v):
        minimal_capacity = edge_to_parent[end_v].capacity
        current_v = end_v
        edge = edge_to_parent[current_v]
        ## find minimal capacity
        while edge is not None:
            minimal_capacity = min(minimal_capacity, edge.capacity)
            current_v = edge.start_v
            edge = edge_to_parent[current_v]
        print(minimal_capacity)
        current_v = end_v
        edge = edge_to_parent[current_v]
        while edge is not None:
            edge.capacity -= minimal_capacity
            self.add_edge(minimal_capacity, edge.end_v, edge.start_v, )
            current_v = edge.start_v
            edge = edge_to_parent[current_v]
        self.flow += minimal_capacity
