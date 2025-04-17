class Solution:
    def uniquePathsWithObstacles(
        self,
        obstacleGrid: list[list[int]],
    ) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = int(obstacleGrid[0][0] == 0)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                if obstacleGrid[i - 1][j - 1] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


if __name__ == "__main__":
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    obstacleGrid = [
        [0, 1],
        [0, 0],
    ]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
