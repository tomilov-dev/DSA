def isBipartiteDFS(adj: list[list[int]]) -> bool:
    def dfs(u: int, c: int) -> bool:
        colors[u] = c
        for v in adj[u]:
            if colors[v] == -1:
                if not dfs(v, 1 - c):
                    return False
            else:
                return False
        return True

    n = len(adj)
    colors = [-1] * n
    for i in range(n):
        if colors[i] != -1:
            continue
        if not dfs(i, 0):
            return False
    return True
