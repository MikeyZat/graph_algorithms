class Edge:
    def __init__(self, capacity, start_v, end_v):
        self.capacity = capacity
        self.residual_capacity = capacity
        self.start_v = start_v
        self.end_v = end_v

    def __str__(self):
        return '(' + str(self.start_v) + ', ' + str(self.end_v) + ', ' + str(self.capacity) + ')'
