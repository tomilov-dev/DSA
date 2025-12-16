class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        MAX = 10**10
        n = 26
        graph = [[MAX] * n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0

        for i in range(len(original)):
            u = ord(original[i]) - ord("a")
            v = ord(changed[i]) - ord("a")
            w = cost[i]
            graph[u][v] = min(graph[u][v], w)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][k] == MAX or graph[k][j] == MAX:
                        continue
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        total = 0
        for i in range(len(source)):
            u = ord(source[i]) - ord("a")
            v = ord(target[i]) - ord("a")
            if u == v:
                continue
            if graph[u][v] == MAX:
                return -1
            total += graph[u][v]
        return total


if __name__ == "__main__":
    res = Solution().minimumCost(
        source="abcd",
        target="acbe",
        original=["a", "b", "c", "c", "e", "d"],
        changed=["b", "c", "b", "e", "b", "e"],
        cost=[2, 5, 5, 1, 2, 20],
    )
