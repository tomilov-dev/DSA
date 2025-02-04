class Solution:
    def allPathsSourceTarget(
        self,
        graph: list[list[int]],
    ) -> list[list[int]]:
        def dfs(node: int) -> list[list[int]]:
            if node in memo:
                return memo[node]
            if node == target:
                return [[target]]

            paths = []
            for child in graph[node]:
                for path in dfs(child):
                    paths.append([node] + path)

            memo[node] = paths
            return paths

        target = len(graph) - 1
        memo = {}
        return dfs(0)


if __name__ == "__main__":
    graph = [[1, 2], [3], [3], []]
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(Solution().allPathsSourceTarget(graph))
