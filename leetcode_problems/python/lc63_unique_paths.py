class Solution:
    def uniquePathsWithObstacles(
        self,
        obstacleGrid: list[list[int]],
    ) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    dp[i + 1][j + 1] = 0
                    continue
                if i == 0 and j == 0:
                    continue

                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]

        return dp[m][n]


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
