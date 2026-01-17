def kosaraju_scc(graph: dict[int, list[int]]) -> list[list[int]]:
    def dfs(
        v: int,
        visited: set,
        stack: list[int],
    ) -> None:
        visited.add(v)
        for u in graph.get(v, []):
            if u not in visited:
                dfs(u, visited, stack)
        stack.append(v)

    def dfs_transposed(
        v: int,
        visited: set,
        component: list[int],
        transposed: dict[int, list[int]],
    ) -> None:
        visited.add(v)
        component.append(v)
        for u in transposed.get(v, []):
            if u not in visited:
                dfs_transposed(u, visited, component, transposed)

    # 1. Первый проход: порядок завершения
    visited: set[int] = set()
    stack: list[int] = []
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, visited, stack)

    # 2. Транспонирование графа
    transposed: dict[int, list[int]] = {}
    for v in graph:
        for u in graph[v]:
            transposed.setdefault(u, []).append(v)

    # 3. Второй проход: поиск компонент
    visited: set[int] = set()
    sccs: list[list[int]] = []
    while stack:
        v = stack.pop()
        if v not in visited:
            component: list[int] = []
            dfs_transposed(v, visited, component, transposed)
            sccs.append(component)
    return sccs


def kosaraju_scc_iterative(graph: dict[int, list[int]]) -> list[list[int]]:
    def dfs_iterative(
        start: int,
        visited: set[int],
        stack: list[int],
    ) -> None:
        local_stack = [start]
        while local_stack:
            v = local_stack[-1]
            if v not in visited:
                visited.add(v)
                for u in graph.get(v, []):
                    if u not in visited:
                        local_stack.append(u)
            else:
                local_stack.pop()
                if v not in stack:
                    stack.append(v)

    def dfs_transposed_iterative(
        start: int,
        visited: set[int],
        component: list[int],
        transposed: dict[int, list[int]],
    ) -> None:
        local_stack = [start]
        while local_stack:
            v = local_stack.pop()
            if v not in visited:
                visited.add(v)
                component.append(v)
                for u in transposed.get(v, []):
                    if u not in visited:
                        local_stack.append(u)

    # 1. Первый проход: порядок завершения
    visited: set[int] = set()
    stack: list[int] = []
    for vertex in graph:
        if vertex not in visited:
            dfs_iterative(vertex, visited, stack)

    # 2. Транспонирование графа
    transposed: dict[int, list[int]] = {}
    for v in graph:
        for u in graph[v]:
            transposed.setdefault(u, []).append(v)

    # 3. Второй проход: поиск компонент
    visited = set()
    sccs: list[list[int]] = []
    while stack:
        v = stack.pop()
        if v not in visited:
            component: list[int] = []
            dfs_transposed_iterative(v, visited, component, transposed)
            sccs.append(component)
    return sccs
