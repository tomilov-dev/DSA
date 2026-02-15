from collections import deque


def isBipartiteBFS(adj: list[list[int]]) -> bool:
    n = len(adj)
    color = [-1] * n
    for i in range(n):
        if color[i] != -1:
            continue

        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[v]:
                if color[v] == -1:
                    # 1 - color[u] -> 0 или 1, то есть обратный color[u]
                    # можно записать как 0 if color[u] == 1 else 1
                    color[v] = 1 - color[u]
                    q.append(v)
                else:
                    return False
    return True
