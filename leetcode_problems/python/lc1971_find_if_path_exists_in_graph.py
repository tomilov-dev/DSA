from collections import deque


class Solution:
    def validPath(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int,
    ) -> bool:
        def dfs(node: int) -> bool:
            nonlocal seen
            if node in seen:
                return False
            if node == destination:
                return True

            seen.add(node)
            for child in adj[node]:
                if dfs(child):
                    return True

            return False

        seen = set()
        adj: dict[int, list[int]] = dict()
        for x, y in edges:
            if x not in adj:
                adj[x] = []
            adj[x].append(y)
            if y not in adj:
                adj[y] = []
            adj[y].append(x)

        return dfs(source)


class SolutionBFS:
    def validPath(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int,
    ) -> bool:
        adj: dict[int, list[int]] = dict()
        for x, y in edges:
            if x not in adj:
                adj[x] = []
            adj[x].append(y)
            if y not in adj:
                adj[y] = []
            adj[y].append(x)

        q = deque([source])
        seen = set()
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in seen:
                    continue
                if node == destination:
                    return True

                seen.add(node)
                for child in adj[node]:
                    q.append(child)

        return False


if __name__ == "__main__":
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    # print(Solution().validPath(n, edges, source, destination))
    print(SolutionBFS().validPath(n, edges, source, destination))
