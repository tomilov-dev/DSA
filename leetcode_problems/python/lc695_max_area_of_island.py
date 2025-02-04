class Solution:
    def maxAreaOfIsland(
        self,
        grid: list[list[int]],
    ) -> int:
        def inbound(
            i: int,
            j: int,
        ) -> bool:
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i: int, j: int) -> int:
            if not inbound(i, j):
                return 0
            if visited[i][j]:
                return 0
            if grid[i][j] == 0:
                return 0

            visited[i][j] = True
            l = dfs(i, j + 1)
            r = dfs(i, j - 1)
            t = dfs(i + 1, j)
            b = dfs(i - 1, j)
            return 1 + l + r + t + b

        visited = [[False] * len(grid[i]) for i in range(len(grid))]
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or visited[i][j]:
                    continue

                maxi = max(maxi, dfs(i, j))

        return maxi


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    print(Solution().maxAreaOfIsland(grid))
