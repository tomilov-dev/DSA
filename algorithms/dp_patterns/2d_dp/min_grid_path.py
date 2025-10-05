MAX = 10**9


class Solution:
    def min_path(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[MAX] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                dp[i][j] = grid[i - 1][j - 1] + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                )
        return dp[m][n]


class SolutionOptimal:
    def min_path(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [MAX] * (n + 1)
        dp[1] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[j] = grid[i - 1][j - 1] + min(dp[j], dp[j - 1])
        return dp[n]
