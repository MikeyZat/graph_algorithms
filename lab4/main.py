from lab2.dimacs import *


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()  # zbiór sąsiadów

    def connect_to(self, v):
        self.out.add(v)



def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            Ni = G[vs[i]].out
            Nj = G[vs[j]].out

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    return False
    return True


def lexBFS(V, G):
    order = [0 for _ in range(V)]
    list_of_sets = [set([i for i in range(1, V + 1)])]
    for i in range(1, V + 1):
        current_vertex = list_of_sets[-1].pop()
        order[i-1] = current_vertex
        new_list_of_sets = []
        for v_set in list_of_sets:
            if v_set:
                difference = v_set - G[current_vertex].out
                multiplication = v_set & G[current_vertex].out
                if difference:
                    new_list_of_sets.append(difference)
                if multiplication:
                    new_list_of_sets.append(multiplication)
    #     print('current vertext', current_vertex)
    #     print('current vertext out', G[current_vertex].out)
    #     print('current list', list_of_sets)
    #     print('new list', new_list_of_sets)
        list_of_sets = new_list_of_sets
    # print(order)
    # print(checkLexBFS(G, order))
    return order


def get_rn_list(order, V, G):
    RN = [ 0 for _ in range(V+1)]
    for i in range(V):
        RN[order[i]] = [ order[j] for j in range (i) if order[j] in G[order[i]].out]
    return RN


def check_if_on(rn, V):
    for i in range(1, V):
        if len(rn[i]) > 0:
            parent = rn[i][-1]
            if not((set(rn[i]) - {parent}) <= set(rn[parent])):
                return False
    return True

(V, L) = loadWeightedGraph('graphs/chordal/k33')
G = [None] + [Node(i) for i in range(1, V + 1)]
for (u, v, _) in L:
    G[u].connect_to(v)
    G[v].connect_to(u)

order = lexBFS(V, G)
RN = get_rn_list(order, V, G)
is_diagonal = check_if_on(RN, V)
