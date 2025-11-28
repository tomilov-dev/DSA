class UnionFindRank:
    """
    Optimized Union Find by rank of tree
    """

    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFindRank(n)
        for x, y in edges:
            uf.union(x, y)

        groups = {}
        for x in range(n):
            root = uf.find(x)
            groups.setdefault(root, []).append(x)

        edge_count = {root: 0 for root in groups}
        for x, y in edges:
            root = uf.find(x)
            edge_count[root] += 1

        res = 0
        for root, nodes in groups.items():
            k = len(nodes)
            if edge_count[root] == k * (k - 1) // 2:
                res += 1
        return res


if __name__ == "__main__":
    res = Solution().countCompleteComponents(
        n=6,
        edges=[[0, 1], [0, 2], [1, 2], [3, 4]],
    )
    print(res)
