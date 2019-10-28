class Edge:
    def __init__(self, capacity, start_v, end_v, correspondive_edge=None):
        self.capacity = capacity
        self.residual_capacity = capacity
        self.start_v = start_v
        self.end_v = end_v
        self.correspondive_edge = correspondive_edge

    def __str__(self):
        return f'({str(self.start_v)}, {str(self.end_v)}, {str(self.capacity)})'
