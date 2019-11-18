import unittest
import os
from lab3.main import ford_fulkerson


def get_result_from_file(graph_dir, file_name):
    f = open(f'{graph_dir}/{file_name}', "r")
    lines = f.readlines()
    result = 0
    for l in lines:
        s = l.split()
        if s[0] == "c":
            result = s[len(s) - 1]
    f.close()
    return int(result)


class FordFulkerson(unittest.TestCase):

    def setUp(self):
        self.graph_dir = "graphs"
        files = os.listdir(self.graph_dir)
        self.results = {}
        for file in files:
            self.results[file] = get_result_from_file(self.graph_dir, file)

    def test_ford_fulkerson(self):
        files = os.listdir("graphs")
        for graph_name in files:
            self.assertEqual(
                self.results.get(graph_name),
                ford_fulkerson(f'{self.graph_dir}/{graph_name}'),
                f'Testing {graph_name}')


if __name__ == '__main__':
    unittest.main()
