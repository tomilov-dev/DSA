from typing import Optional


def topological_sort(
    graph: list[list[int]],
    start_vertex: int,
) -> list:
    def dfs(vertex: int) -> None:
        color[vertex] = "g"
        for child_vertex in range(len(graph)):
            if graph[vertex][child_vertex] == 1 and color[child_vertex] == "w":
                color[child_vertex] = "g"
                dfs(child_vertex)

        color[vertex] = "b"
        stack.append(vertex)

    stack = []
    color = ["w" for _ in range(len(graph))]
    dfs(start_vertex)
    return stack[::-1]


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

    gsort = topological_sort(adj_matrix, start_vertex)
    print(gsort)
