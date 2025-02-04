class Solution:
    def minPathSum(
        self,
        grid: list[list[int]],
    ) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i + 1][j + 1] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])

        return dp[m][n]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # grid = [[1, 2, 3], [4, 5, 6]]
    print(Solution().minPathSum(grid))
