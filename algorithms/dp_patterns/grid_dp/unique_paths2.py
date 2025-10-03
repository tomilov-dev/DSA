class Solution:
    def uniquePathsWithObstacles(
        self,
        obstacleGrid: list[list[int]],
    ) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                if obstacleGrid[i - 1][j - 1]:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m][n]


class SolutionOptimal:
    def uniquePathsWithObstacles(
        self,
        obstacleGrid: list[list[int]],
    ) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0] * n
        prev[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                left = curr[j - 1] if j > 0 else 0
                curr[j] = prev[j] + left
                if obstacleGrid[i][j]:
                    curr[j] = 0
            prev = curr
        return prev[n - 1]
