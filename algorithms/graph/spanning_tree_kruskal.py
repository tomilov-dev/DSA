import sys
from pathlib import Path

PROJ_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJ_DIR))
from data_structures.union_find import UnionFindRank


def kruskal(
    n: int,
    edges: list[tuple[int, int, int]],
) -> tuple[list[tuple[int, int, int]], int]:
    edges.sort(key=lambda x: x[2])
    uf = UnionFindRank(n)
    mst: list[tuple[int, int, int]] = []
    total_weight: int = 0
    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break
    return mst, total_weight
