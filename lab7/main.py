import networkx as nx  # standardowy sposób importowania biblioteki
from networkx.algorithms.flow import maximum_flow
from networkx.algorithms.planarity import check_planarity
from lab7.dimacs import *


def load_directed_graph(graph_path):
    (V, L) = loadDirectedWeightedGraph(graph_path)
    G = nx.DiGraph()
    for (start_v, end_v, capacity) in L:
        G.add_edge(start_v, end_v)
    return G, V, L


def load_graph(graph_path):
    (V, L) = loadWeightedGraph(graph_path)
    G = nx.Graph()
    for (start_v, end_v) in L:
        G.add_edges_from([(start_v, end_v), (end_v, start_v)])
    return G, V, L


def add_capacity(G, L):
    for (start_v, end_v, capacity) in L:
        G[start_v][end_v]['capacity'] = capacity


def find_max_flow(G, V, L):
    add_capacity(G, L)
    value, flow = maximum_flow(G, 1, V)
    return value


def check_planar(G): return check_planarity(G)[0]


G1, V1, L1 = load_directed_graph('graphs-lab6/plnar/clique20')
G2, V2, L2 = load_directed_graph('graphs-lab2/flow/simple')
print(check_planar(G1))
print(find_max_flow(G2, V2, L2))



