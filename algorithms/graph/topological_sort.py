from collections import deque


def topological_sort_dfs(graph: list[list[int]]) -> list:
    def dfs(vertex: int) -> None:
        color[vertex] = 1
        for child, conn in enumerate(graph[vertex]):
            if conn == 1 and color[child] == 0:
                dfs(child)
        color[vertex] = 2
        stack.append(vertex)

    n = len(graph)
    stack = []
    color = [0] * n
    for v in range(len(graph)):
        if color[v] == 0:
            dfs(v)
    return stack[::-1]


def topological_sort_kahn(graph: list[list[int]]) -> list:
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v, conn in enumerate(graph[u]):
            if conn == 0:
                continue
            in_degree[v] += 1

    q = deque([i for i in range(n) if in_degree[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v, conn in enumerate(graph[u]):
            if conn == 0:
                continue
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(order) != n:
        return []
    return order


if __name__ == "__main__":
    adj_matrix = [
        [0, 1, 1, 0, 0, 0],  # Вершина 0
        [0, 0, 0, 1, 0, 0],  # Вершина 1
        [0, 0, 0, 1, 1, 0],  # Вершина 2
        [0, 0, 0, 0, 0, 1],  # Вершина 3
        [0, 0, 0, 0, 0, 1],  # Вершина 4
        [0, 0, 0, 0, 0, 0],  # Вершина 5
    ]
    start_vertex = 0

    gsort = topological_sort_dfs(adj_matrix)
    print(gsort)
