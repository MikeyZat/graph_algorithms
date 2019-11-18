class Vertex:
    def __init__(self):
        self.edges = {}  # słownik par mapujący wierzchołki do których są krawędzie na ich wagi
        self.merged = False

    def add_edge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight  # dodaj krawędź do zadanego wierzchołka
        # o zadanej wadze; a jeśli taka krawędź
        # istnieje, to dodaj do niej wagę

    def del_edge(self, to):
        del self.edges[to]

    def set_merged(self):
        self.edges = {}
        self.merged = True

    def __str__(self):
        representation = 'Merged: ' + str(self.merged) + '\n'
        for key in self.edges.keys():
            representation += 'edge to:' + str(key) + ' with value ' + str(self.edges[key]) + '\n'
        return representation
