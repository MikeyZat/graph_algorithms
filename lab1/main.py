def load_weighted_graph(name):
    """Load a graph in the DIMACS ascii format (with weights) from
     the file "name" and return it as a list of sets
     Returns (V,L)
     V -- number of vertices (1, ..., V)
     L -- list of edges in the format (x,y,w): edge between x and y with weight w (x<y)"""

    V = 0
    L = []

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if len(s) < 1: continue
        if s[0] == "c":
            continue
        elif s[0] == "p":
            V = int(s[2])
        elif s[0] == "e":
            (a, b, c) = (int(s[1]), int(s[2]), int(s[3]))
            (x, y, c) = (min(a, b), max(a, b), c)
            L.append((x, y, c))

    f.close()
    return (V, L)


def find(i, union_list):
    while union_list[i][0] != i:
        i = union_list[i][0]
    return i


def union(i, j, union_list):
    i = find(i, union_list)
    j = find(j, union_list)
    rank_i = union_list[i][1]
    rank_j = union_list[j][1]

    if rank_i == rank_j:
        union_list[i][0] = j
        union_list[j][1] += 1
    elif rank_i > rank_j:
        union_list[j][0] = i
    else:
        union_list[i][0] = j


def sort_descending(L):
    L.sort(key=lambda x: x[2], reverse=True)


def print_graph(L):
    for (x, y, c) in L:  # przeglądaj krawędzie z listy
        print("krawedz miedzy", x, "i", y, "o wadze", c)  # wypisuj


def test_find_union(union_list):
    print(union_list)
    union(1, 2, union_list)
    print(union_list)
    union(3, 4, union_list)
    print(union_list)
    union(2, 3, union_list)
    print(union_list)


# main

(V, L) = load_weighted_graph("rand100_500")
union_list = [[i, 0] for i in range(V+1)]
sort_descending(L)

result = L[0][2]

for edge in L:
    union(edge[0], edge[1], union_list)
    result = min(edge[2], result)
    if union_list[1][0] == union_list[V][0]:
        print(result)
        break



