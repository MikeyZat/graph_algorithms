class Vertex:
    def __init__(self, i):
        self.edges = {}  # słownik par mapujący wierzchołki do których są krawędzie na ich wagi
        self.merged = False
        self.index = i

    def add_edge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight  # dodaj krawędź do zadanego wierzchołka
        # o zadanej wadze; a jeśli taka krawędź
        # istnieje, to dodaj do niej wagę

    def del_edge(self, to):
        try:
            del self.edges[to]
        except:
            print("ERROR WHILE DELETING")
            print(self.index)
            print(to)
            Exception()

    def set_merged(self):
        self.edges = {}
        self.merged = True

    def __str__(self):
        representation = 'Merged: ' + str(self.merged) + '\n'
        for key in self.edges.keys():
            representation += 'edge to:' + str(key) + ' with value ' + str(self.edges[key]) + '\n'
        return representation
