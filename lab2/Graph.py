from lab2.Edge import *


class Graph:
    def __init__(self, size, is_residual=False):
        self.vertices_list = [[] for _ in range(size + 1)]
        self.size = size + 1
        self.flow = 0
        self.is_residual = is_residual

    def add_edge(self, capacity, start_v, end_v):
        edge = Edge(capacity, start_v, end_v)
        if self.is_residual:
            back_edge = Edge(0, end_v, start_v)
            edge.correspondive_edge = back_edge
            back_edge.correspondive_edge = edge
            self.vertices_list[end_v].append(
                back_edge
            )
        self.vertices_list[start_v].append(
            edge
        )

    def update(self, edge_to_parent, end_v):
        if self.is_residual:
            minimal_capacity = self.find_minimal_capacity(edge_to_parent, end_v)
            self.update_capacities(edge_to_parent, end_v, minimal_capacity)
            self.flow += minimal_capacity

    def find_minimal_capacity(self, edge_to_parent, end_v):
        current_v = end_v
        edges = edge_to_parent[current_v]
        minimal_capacity = edges[0].capacity
        while edges is not None:
            (edge, correspondive_edge) = edges
            minimal_capacity = min(minimal_capacity, edge.capacity)
            current_v = correspondive_edge.end_v
            edges = edge_to_parent[current_v]
        return minimal_capacity

    def update_capacities(self, edge_to_parent, end_v, minimal_capacity):
        current_v = end_v
        edges = edge_to_parent[current_v]
        while edges is not None:
            (edge, correspondive_edge) = edges
            edge.capacity -= minimal_capacity
            correspondive_edge.capacity += minimal_capacity
            current_v = correspondive_edge.end_v
            edges = edge_to_parent[current_v]