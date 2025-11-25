def undirect(graph: list[list[int]]) -> bool:
    def dfs(v: int, parent: int) -> bool:
        color[v] = 1
        for child, conn in enumerate(graph[v]):
            if conn == 0:
                continue

            if color[child] == 0:
                if dfs(child, v):
                    return True
            elif child != parent:
                return True

        color[v] = 2
        return False

    n = len(graph)
    color = [0] * n
    for v in range(n):
        if color[v] == 0 and dfs(v, -1):
            return True
    return False


def direct(graph: list[list[int]]) -> bool:
    def dfs(v: int) -> bool:
        color[v] = 1
        for child, conn in enumerate(graph[v]):
            if conn == 0:
                continue

            if color[child] == 0:
                if dfs(child):
                    return True
            elif color[child] > 0:
                return True

        color[v] = 2
        return False

    n = len(graph)
    color = [0] * n
    for v in range(n):
        if color[v] == 0 and dfs(v):
            return True
    return False
