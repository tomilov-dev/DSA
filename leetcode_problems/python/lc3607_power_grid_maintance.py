class UnionFindRank:
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
    def processQueries(
        self,
        c: int,
        connections: list[list[int]],
        queries: list[list[int]],
    ) -> list[int]:
        uf = UnionFindRank(c + 1)
        for x, y in connections:
            uf.union(x, y)

        online = [True] * (c + 1)
        components: dict[int, list[int]] = dict()
        for x in range(1, c + 1):
            root = uf.find(x)
            if root not in components:
                components[root] = []
            components[root].append(x)
        for k, v in components.items():
            components[k] = list(reversed(v))

        res = []
        for cmd, x in queries:
            if cmd == 1 and online[x]:
                res.append(x)

            elif cmd == 1 and not online[x]:
                root = uf.find(x)
                grid = components[root]
                if len(grid) == 0:
                    res.append(-1)
                    continue

                while len(grid) > 0 and not online[grid[-1]]:
                    grid.pop()
                if len(grid) > 0:
                    res.append(grid[-1])
                else:
                    res.append(-1)

            elif cmd == 2:
                online[x] = False

        return res
