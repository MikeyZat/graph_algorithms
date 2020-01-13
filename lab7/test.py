import unittest
import os
from lab7.main import *


def get_result_from_file(graph_dir, file_name):
    f = open(f'{graph_dir}/{file_name}', "r")
    lines = f.readlines()
    result = 0
    for l in lines:
        s = l.split('=')
        result = s[len(s) - 1]
    f.close()
    print(result)
    return int(result)


def prepare_data(graph_dir, file_name):
    G, V = load_formula(f'{graph_dir}/{file_name}')
    return G, V


class FormulaTest(unittest.TestCase):

    def prepare(self, graph_dir):
        files = os.listdir(graph_dir)
        self.results = {}
        for file in files:
            self.results[file] = get_result_from_file(graph_dir, file)

    def test_is_diagonal(self):
        self.prepare("sat")
        files = os.listdir("sat")
        for graph_name in files:
            G, V = prepare_data("sat", graph_name)
            self.assertEqual(
                self.results.get(graph_name),
                check_if_fulfillable(G),
                f'Testing {graph_name}')


if __name__ == '__main__':
    unittest.main()
