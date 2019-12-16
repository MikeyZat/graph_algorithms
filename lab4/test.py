import unittest
import os
from lab4.main import *
from lab2.dimacs import *


def get_result_from_file(graph_dir, file_name):
    f = open(f'graphs/{graph_dir}/{file_name}', "r")
    lines = f.readlines()
    result = 0
    for l in lines:
        s = l.split()
        if s[0] == "c":
            result = s[len(s) - 1]
    f.close()
    return int(result)


def prepare_data(graph_dir, file_name):
    (V, L) = loadWeightedGraph(f'graphs/{graph_dir}/{file_name}')

    G = [None] + [Node(i) for i in range(1, V + 1)]
    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)

    order = lexBFS(V, G)
    RN = get_rn_list(order, V, G)
    return RN, order, V, G


class DiagonalGraphs(unittest.TestCase):

    def prepare(self, graph_dir):
        files = os.listdir("graphs/" + graph_dir)
        self.results = {}
        for file in files:
            self.results[file] = get_result_from_file(graph_dir, file)

    def test_lex_bfs(self):
        files = os.listdir("graphs/coloring")
        for graph_name in files:
            RN, lexBFS_order, V, G = prepare_data("chordal", graph_name)
            self.assertTrue(
                checkLexBFS(G, lexBFS_order),
                f'Testing {graph_name}')

    def test_is_diagonal(self):
        self.prepare("chordal")
        files = os.listdir("graphs/chordal")
        for graph_name in files:
            RN, lexBFS_order, V, G = prepare_data("chordal", graph_name)
            self.assertEqual(
                self.results.get(graph_name),
                check_if_on(RN, V),
                f'Testing {graph_name}')

    def test_max_clique_size(self):
        self.prepare("maxclique")
        files = os.listdir("graphs/maxclique")
        for graph_name in files:
            RN, lexBFS_order, V, G = prepare_data("maxclique", graph_name)
            self.assertEqual(
                self.results.get(graph_name),
                find_max_clique(RN)[0],
                f'Testing {graph_name}')

    def test_coloring(self):
        self.prepare("coloring")
        files = os.listdir("graphs/coloring")
        for graph_name in files:
            RN, lexBFS_order, V, G = prepare_data("coloring", graph_name)
            self.assertEqual(
                self.results.get(graph_name),
                paint_graph(lexBFS_order, V, G)[1],
                f'Testing {graph_name}')

    def test_cover(self):
        self.prepare("vcover")
        files = os.listdir("graphs/vcover")
        for graph_name in files:
            RN, lexBFS_order, V, G = prepare_data("vcover", graph_name)
            self.assertEqual(
                self.results.get(graph_name),
                V - len(find_max_independent_set(lexBFS_order, G)),
                f'Testing {graph_name}')


if __name__ == '__main__':
    unittest.main()
