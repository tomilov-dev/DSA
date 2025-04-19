class Solution:
    def minPathSum(
        self,
        grid: list[list[int]],
    ) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[10**5] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                c = grid[i - 1][j - 1]
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + c
        return dp[m][n]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    grid = [[1, 2, 3], [4, 5, 6]]
    print(Solution().minPathSum(grid))
