def find_eulerian_path_hierholzer(adj: list[list[int]]) -> list[int]:
    n = len(adj)
    odd = [i for i in range(n) if sum(adj[i]) % 2 == 1]
    start = odd[0] if odd else 0
    stack = [start]
    path = []
    g = [row[:] for row in adj]
    while stack:
        u = stack[-1]
        for v in range(n):
            if g[u][v]:
                g[u][v] -= 1
                g[v][u] -= 1
                stack.append(v)
                break
        else:
            path.append(stack.pop())
    path.reverse()
    return path


def find_eulerian_path_directed_hierholzer(adj: list[list[int]]) -> list[int]:
    n = len(adj)
    out_deg = [sum(adj[i]) for i in range(n)]
    in_deg = [sum(adj[j][i] for j in range(n)) for i in range(n)]
    start = 0
    for i in range(n):
        if out_deg[i] - in_deg[i] == 1:
            start = i
            break

    stack = [start]
    path = []
    g = [row[:] for row in adj]
    while stack:
        u = stack[-1]
        for v in range(n):
            if g[u][v]:
                g[u][v] -= 1
                stack.append(v)
                break
        else:
            path.append(stack.pop())
    path.reverse()
    return path
