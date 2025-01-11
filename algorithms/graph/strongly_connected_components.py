def transpone_graph(
    graph: list[list[int]],
) -> list[list[int]]:
    transponed = [[0] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            transponed[j][i] = graph[i][j]
    return transponed


def strongly_connected_components(graph: list[list[int]]):
    def dfs(
        graph: list[list[int]],
        vertex: int,
        stack: list[int] | None = None,
        component: list[int] | None = None,
    ) -> None:
        color[vertex] = "g"
        if component is not None:
            component.append(vertex)

        for cv in range(len(graph)):
            if graph[vertex][cv] == 1 and color[cv] == "w":
                dfs(graph, cv, stack, component)
        color[vertex] = "b"

        if stack is not None:
            stack.append(vertex)

    color = ["w"] * len(graph)
    stack = []
    for v in range(len(graph)):
        if color[v] == "w":
            dfs(graph, v, stack)

    transponed_graph = transpone_graph(graph)
    color = ["w"] * len(graph)
    scc = []
    while stack:
        vertex = stack.pop()
        if color[vertex] == "w":
            component = []
            dfs(transponed_graph, vertex, component=component)
            scc.append(component)

    return scc


if __name__ == "__main__":
    adj_matrix = [
        [0, 1, 0, 0],  # Вершина 0
        [0, 0, 1, 0],  # Вершина 1
        [1, 0, 0, 0],  # Вершина 2
        [0, 0, 0, 1],  # Вершина 3
    ]

    adj_matrix = [
        [0, 1, 0, 0],  # Вершина 0
        [0, 0, 1, 0],  # Вершина 1
        [0, 0, 0, 0],  # Вершина 2
        [0, 0, 1, 0],  # Вершина 3
    ]

    adj_matrix = [
        [0, 1, 0, 0, 0, 0],  # Вершина 0
        [0, 0, 1, 0, 0, 0],  # Вершина 1
        [1, 0, 0, 1, 0, 0],  # Вершина 2
        [0, 0, 0, 0, 1, 0],  # Вершина 3
        [0, 0, 0, 0, 0, 1],  # Вершина 4
        [0, 0, 0, 0, 0, 0],  # Вершина 5
    ]

    adj_matrix = [
        [0, 1, 0, 0, 0],  # Вершина 0
        [0, 0, 1, 0, 0],  # Вершина 1
        [0, 0, 0, 1, 0],  # Вершина 2
        [0, 0, 0, 0, 1],  # Вершина 3
        [1, 0, 0, 0, 0],  # Вершина 4
    ]

    scc = strongly_connected_components(adj_matrix)
    print(scc)
