def hamiltonian_path_backtracking(adj: list[list[int]]) -> list[int] | None:
    def backtrack(v: int, visited: set[int]) -> bool:
        path.append(v)
        if len(path) == n:
            return True
        for u in range(n):
            if adj[v][u] and u not in visited:
                if backtrack(u, visited | {u}):
                    return True
        path.pop()
        return False

    n = len(adj)
    path = []
    for start in range(n):
        path.clear()
        if backtrack(start, {start}):
            return path
    return None


def hamiltonian_path_dp(adj: list[list[int]]) -> bool:
    n = len(adj)
    dp = [[False] * n for _ in range(1 << n)]
    for v in range(n):
        dp[1 << v][v] = True

    for mask in range(1 << n):
        for v in range(n):
            if not dp[mask][v]:
                continue
            for u in range(n):
                if not adj[v][u]:
                    continue
                if mask & (1 << u):
                    continue
                dp[mask | (1 << u)][u] = True

    full = (1 << n) - 1
    return any(dp[full][v] for v in range(n))
