class SolutionBottomUp:
    def numberOfPaths(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1 if grid[0][0] == 0 else 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                if grid[i - 1][j - 1] == 1:
                    grid[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


class SolutionBottomUpOptimized:
    def numberOfPaths(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n
        dp[0] = 1 if grid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[n - 1]


if __name__ == "__main__":
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print(SolutionBottomUp().numberOfPaths(grid))
    print(SolutionBottomUpOptimized().numberOfPaths(grid))
