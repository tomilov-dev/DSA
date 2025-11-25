def adjacency_matrix_recursive(graph: list[list[int]], initial: int = 0):
    def dfs(vertex: int):
        nonlocal time

        time += 1
        start[vertex] = time
        color[vertex] = 1
        for child, conn in enumerate(graph[vertex]):
            if conn == 1 and color[child] == 0:
                parent[child] = vertex
                dfs(child)

        time += 1
        finish[vertex] = time
        color[vertex] = 2

    n = len(graph)
    color = [0] * n
    time = 0
    start: list[int] = [-1] * n
    finish: list[int] = [-1] * n
    parent: list[int] = [-1] * n
    dfs(initial)


def adjacency_matrix(graph: list[list[int]], initial: int = 0):
    n = len(graph)
    color = [0] * n
    time = 0
    start: list[int] = [-1] * n
    finish: list[int] = [-1] * n
    parent: list[int] = [-1] * n

    stack = [initial]
    while stack:
        vertex = stack.pop()
        ## Проверка избыточна, т.к. в стеке заведомо только color[v] = 0
        if color[vertex] > 0:
            continue

        time += 1
        start[vertex] = time
        color[vertex] = 1
        ## Соблюдаем строго обратный порядок обхода узлов
        for child, conn in enumerate(graph[vertex][::-1]):
            if conn == 1 and color[child] == 0:
                parent[child] = vertex
                stack.append(child)

        time += 1
        finish[vertex] = time
        color[vertex] = 2


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    start_vertex = 0
    adjacency_matrix_recursive(graph, start_vertex)
    adjacency_matrix(graph, start_vertex)
