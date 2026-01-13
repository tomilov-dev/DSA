def all_paths(
    graph: list[list[int]],
    start: int,
    end: int,
) -> list[list[int]]:
    def dfs(v: int) -> None:
        path.append(v)
        if v == end:
            result.append(path[:])
        else:
            for to in graph[v]:
                if to not in path:
                    dfs(to)
        path.pop()

    result: list[list[int]] = []
    path: list[int] = []

    dfs(start)
    return result
