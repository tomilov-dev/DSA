def dfs_adjacency_matrix_recursive(
    graph: list[list[int]],
    start_vertex: int,
) -> None:
    def dfs(vertex: int):
        nonlocal time

        time += 1
        color[vertex] = "g"
        discovery_time[vertex] = time
        for child_vertex in range(len(graph[vertex])):
            if graph[vertex][child_vertex] == 1 and color[child_vertex] == "w":
                parent[child_vertex] = vertex
                dfs(child_vertex)

        time += 1
        color[vertex] = "b"
        finish_time[vertex] = time

    color = ["w" for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]
    discovery_time = [None for _ in range(len(graph))]
    finish_time = [None for _ in range(len(graph))]
    time = 0

    dfs(start_vertex)
    print("Color:", color)
    print("Parent:", parent)
    print("Discovery Time:", discovery_time)
    print("Finish Time:", finish_time)


def dfs_adjacency_list_recursive(
    graph: dict[int, list[int]],
    start_vertex: int,
) -> None:
    def dfs(vertex: int):
        nonlocal time

        time += 1
        discovery_time[vertex] = time
        color[vertex] = "g"
        for child_vertex in graph[vertex]:
            if color[child_vertex] == "w":
                parent[child_vertex] = vertex
                dfs(child_vertex)

        time += 1
        finish_time[vertex] = time
        color[vertex] = "b"

    color = {v: "w" for v in graph}
    parent = {v: None for v in graph}
    discovery_time = {v: None for v in graph}
    finish_time = {v: None for v in graph}
    time = 0

    dfs(start_vertex)
    print("Color:", color)
    print("Parent:", parent)
    print("Discovery Time:", discovery_time)
    print("Finish Time:", finish_time)


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    start_vertex = 0
    dfs_adjacency_matrix_recursive(graph, start_vertex)

    # graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    # start_vertex = 0
    # dfs_adjacency_list_recursive(graph, start_vertex)
