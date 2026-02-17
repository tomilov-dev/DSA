from typing import List, Tuple, Dict, Any


def stoer_wagner(graph: List[List[Tuple[int, int]]]) -> Dict[str, Any]:
    """
    graph: adjacency list for undirected weighted graph:
           graph[u] = [(v, w), ...]  (weights added if multiple edges)
    returns: {"cut_value": int, "S": list[int], "T": list[int]}
    """
    n = len(graph)
    if n == 0:
        return {"cut_value": 0, "S": [], "T": []}

    W = [[0] * n for _ in range(n)]
    for u, neigh in enumerate(graph):
        for v, w in neigh:
            W[u][v] += w
            W[v][u] += w

    comp = [set([i]) for i in range(n)]  # components of original vertices
    vertices = list(range(n))  # active vertices

    best_value = float("inf")
    best_S = None

    while len(vertices) > 1:
        m = len(vertices)
        added = [False] * m
        weights = [0] * m
        prev = -1
        for iteration in range(m):
            sel = -1
            for i in range(m):
                if not added[i] and (sel == -1 or weights[i] > weights[sel]):
                    sel = i

            added[sel] = True
            if iteration == m - 1:
                # last added = t, prev is s
                cut_weight = weights[sel]
                # build A = union of components of added vertices
                A = set()
                for i in range(m):
                    if added[i]:
                        A |= comp[vertices[i]]
                if cut_weight < best_value:
                    best_value = cut_weight
                    best_S = set(A)
                # merge t into prev
                s_idx = prev
                t_idx = sel
                s = vertices[s_idx]
                t = vertices[t_idx]
                # merge weights of t into s
                for i in vertices:
                    W[s][i] += W[t][i]
                    W[i][s] = W[s][i]
                # merge component sets
                comp[s] |= comp[t]
                # remove t from active vertices
                vertices.pop(t_idx)
                break
            prev = sel
            # increase weights by connections from newly added vertex
            for j in range(m):
                if not added[j]:
                    weights[j] += W[vertices[sel]][vertices[j]]

    if best_S is None:
        best_S = set([0])
    S = sorted(best_S)
    T = sorted(set(range(n)) - best_S)
    return {"cut_value": int(best_value), "S": S, "T": T}


if __name__ == "__main__":
    graph = [
        [(1, 3), (2, 1)],
        [(0, 3), (2, 3), (3, 1)],
        [(0, 1), (1, 3), (3, 4)],
        [(1, 1), (2, 4)],
    ]
    res = stoer_wagner(graph)
    print("cut_value:", res["cut_value"])
    print("S:", res["S"])
    print("T:", res["T"])
