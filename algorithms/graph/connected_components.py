import sys
from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))
from data_structures.union_find import UnionFind


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


def connected_components_count_uf(graph: list[list[int]]) -> int:
    n = len(graph)
    uf = UnionFind(n)
    for v in range(n):
        for u, conn in enumerate(graph[v]):
            if conn == 0:
                continue
            uf.union(v, u)
    roots = set(uf.find(i) for i in range(n))
    return len(roots)


def connected_components_uf(graph: list[list[int]]) -> list[list[int]]:
    n = len(graph)
    uf = UnionFind(n)
    for v in range(n):
        for u, conn in enumerate(graph[v]):
            if conn == 0:
                continue
            uf.union(v, u)

    groups = {}
    for i in range(n):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    return list(groups.values())
