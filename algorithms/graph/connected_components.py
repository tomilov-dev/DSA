def connected_components_count(graph: list[list[int]]) -> int:
    def dfs(v: int):
        color[v] = 1
        for child, conn in enumerate(graph[v]):
            if conn == 1 and color[child] == 0:
                dfs(child)
        color[v] = 2

    n = len(graph)
    color = [0] * n
    components = 0
    for v in range(n):
        if color[v] == 0:
            components += 1
            dfs(v)
    return components


def connected_components(graph: list[list[int]]) -> list[list[int]]:
    def dfs(v: int, comp: list[int]):
        color[v] = 1
        comp.append(v)
        for child, conn in enumerate(graph[v]):
            if conn == 1 and color[child] == 0:
                dfs(child, comp)
        color[v] = 2

    n = len(graph)
    color = [0] * n
    components: list[list[int]] = []
    for v in range(n):
        if color[v] == 0:
            comp = []
            dfs(v, comp)
            components.append(comp)
    return components
