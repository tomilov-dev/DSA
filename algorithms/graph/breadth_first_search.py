from collections import deque
from collections import defaultdict


def bfs_adjacency_matrix(
    graph: list[list[int]],
    start_vertex: int = 0,
):
    color = ["w"] * len(graph)
    distance = [float("inf")] * len(graph)
    parent = [None] * len(graph)

    color[start_vertex] = "g"
    distance[start_vertex] = 0
    q = deque([start_vertex])

    while q:
        cur_vertex = q.popleft()
        for child_vertex in range(len(graph[cur_vertex])):
            if graph[cur_vertex][child_vertex] == 1 and color[child_vertex] == "w":
                color[child_vertex] = "g"
                distance[child_vertex] = distance[cur_vertex] + 1
                parent[child_vertex] = cur_vertex
                q.append(child_vertex)
        color[cur_vertex] = "b"

    print("Colors:", color)
    print("Distances:", distance)
    print("Parents:", parent)


def bfs_adjacency_list(
    graph: dict[int, list[int]],
    start_vertex: int,
):
    color = {vertex: "w" for vertex in graph}
    distance = {vertex: float("inf") for vertex in graph}
    parent = {vertex: None for vertex in graph}

    color[start_vertex] = "g"
    distance[start_vertex] = 0
    q = deque([start_vertex])

    while q:
        cur_vertex = q.popleft()
        for child_vertex in graph[cur_vertex]:
            if color[child_vertex] == "w":
                color[child_vertex] = "g"
                distance[child_vertex] = distance[cur_vertex] - 1
                parent[child_vertex] = cur_vertex
                q.append(child_vertex)

        color[cur_vertex] = "b"

    print("Colors:", color)
    print("Distances:", distance)
    print("Parents:", parent)


def bfs_edges(
    edges: list[tuple[int, int]],
    start_vertex: int,
):
    num_vertices = get_num_vertices(edges)
    graph = edges_to_adjacency_matrix(edges, num_vertices)
    bfs_adjacency_matrix(graph, start_vertex)


def get_num_vertices(edges: list[tuple[int, int]]) -> int:
    vertices = set()
    for u, v in edges:
        vertices.add(u)
        vertices.add(v)
    return len(vertices)


def edges_to_adjacency_matrix(
    edges: list[tuple[int, int]],
    num_vertices: int,
) -> list[list[int]]:
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix


def edges_to_adjacency_list(
    edges: list[tuple[int, int]],
    num_vertices: int,
) -> dict[int, list[int]]:
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    start_vertex = 0
    bfs_adjacency_matrix(graph, start_vertex)

    # graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    # start_vertex = 0
    # bfs_adjacency_list()
