def tarjan_bridges_cutpoins(
    graph: list[list[int]],
) -> tuple[list[tuple[int, int]], set[int]]:
    def dfs(v: int, p: int):
        nonlocal time

        children = 0
        tin[v] = time
        low[v] = time
        time += 1
        for to in graph[v]:
            if to == p:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append((v, to))
                if low[to] >= tin[v] and p != -1:
                    cutpoints.add(v)
                children += 1
        if p == -1 and children > 1:
            cutpoints.add(v)

    n = len(graph)
    tin = [-1] * n
    low = [-1] * n
    time = 0
    bridges: list[tuple[int, int]] = []
    cutpoints: set[int] = set()
    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
    return bridges, cutpoints
