import networkx as nx  # standardowy sposób importowania biblioteki
from networkx.algorithms.flow import maximum_flow
from networkx.algorithms.planarity import check_planarity
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort
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


def load_formula(formula_path):
    (V, F) = loadCNFFormula(formula_path)
    G = nx.DiGraph()
    for (u, v) in F:
        G.add_edges_from([(-u, v), (-v, u)])
    return G, V


def check_if_fulfillable(SCC):
    for S in SCC:
        component_set = set()
        for v in S:
            if -v in component_set:
                return False
            component_set.add(v)
    return True


def create_components_graph(G, SCC):
    SCC_list = []
    SCC_map = {}
    SCC_G = nx.DiGraph()
    t = 0
    for S in SCC:
        SCC_list.append(S)
        for v in S:
            SCC_map[v] = t
        t += 1
    for (u, v) in G.edges:
        if SCC_map[u] != SCC_map[v]:
            SCC_G.add_edge(SCC_map[u], SCC_map[v])


def zad3():
    G, V = load_formula('sat/sat100_200')
    SCC = strongly_connected_components(G)
    print(check_if_fulfillable(SCC))
    SCC_G = create_components_graph(G, SCC)
    sorted_SCC_G = topological_sort(SCC_G)

    # G1, V1, L1 = load_directed_graph('graphs-lab6/plnar/clique20')
# G2, V2, L2 = load_directed_graph('graphs-lab2/flow/simple')
# print(check_planar(G1))
# print(find_max_flow(G2, V2, L2))

