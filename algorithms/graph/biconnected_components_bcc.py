def tarjan_biconnected_components(
    graph: list[list[int]],
) -> list[list[tuple[int, int]]]:
    def dfs(v: int, p: int):
        nonlocal time

        children = 0
        tin[v] = time
        low[v] = time
        time += 1
        for to in graph[v]:
            if to == p:
                continue
            if tin[to] == -1:
                stack.append((v, to))
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] >= tin[v]:
                    component = []
                    while stack:
                        e = stack.pop()
                        component.append(e)
                        if e == (v, to) or e == (to, v):
                            break
                    bcc.append(component)
                children += 1
            elif tin[to] < tin[v]:
                stack.append((v, to))
                low[v] = min(low[v], tin[to])

    n = len(graph)
    tin = [-1] * n
    low = [-1] * n
    time = 0
    stack: list[tuple[int, int]] = []
    bcc: list[list[tuple[int, int]]] = []
    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
    return bcc
