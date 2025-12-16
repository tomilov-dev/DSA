from collections import deque


def adjacency_matrix(graph: list[list[int]], initial: int = 0):
    n = len(graph)
    MAX = n * n

    color = [0] * n
    distance = [MAX] * n
    parent = [-1] * n

    color[initial] = 1
    distance[initial] = 0
    q = deque([initial])
    while q:
        vertex = q.popleft()
        for child, conn in enumerate(graph[vertex]):
            if conn == 1 and color[child] == 0:
                color[child] = 1
                distance[child] = 1 + distance[vertex]
                parent[child] = vertex
                q.append(child)
        color[vertex] = 2


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    start_vertex = 0
    adjacency_matrix(graph, start_vertex)
