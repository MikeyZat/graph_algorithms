from lab3.Vertex import Vertex


class Graph:
    def __init__(self, size):
        self.vertices_list = [Vertex() for _ in range(size + 1)]
        self.size = size + 1

    def add_edge(self, start_v, end_v, capacity):
        self.vertices_list[start_v].add_edge(end_v, capacity)
        self.vertices_list[end_v].add_edge(start_v, capacity)

    def merge_vertices(self, first_v, second_v):
        edges_to_change = self.vertices_list[second_v].edges
        keys = edges_to_change.keys()
        for key in keys:
            self.vertices_list[first_v].add_edge(key, edges_to_change[key])
            self.vertices_list[key].add_edge(first_v, edges_to_change[key])
            self.vertices_list[key].del_edge(second_v)

        self.vertices_list[second_v].set_merged()
