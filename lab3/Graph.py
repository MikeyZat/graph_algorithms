from lab3.Vertex import Vertex


class Graph:
    def __init__(self, size):
        self.size = size
        self.vertices_list = [Vertex(i) for i in range(self.size + 1)]

    def add_edge(self, start_v, end_v, capacity):
        self.vertices_list[start_v].add_edge(end_v, capacity)
        self.vertices_list[end_v].add_edge(start_v, capacity)

    def merge_vertices(self, first_v, second_v):
        edges_to_change = self.vertices_list[second_v].edges
        for key, value in edges_to_change.items():
            if key == first_v:
                continue
            self.vertices_list[first_v].add_edge(key, value)
            self.vertices_list[key].add_edge(first_v, value)
            self.vertices_list[key].del_edge(second_v)

        self.vertices_list[first_v].del_edge(second_v)
        self.vertices_list[second_v].set_merged()
        self.size -= 1

