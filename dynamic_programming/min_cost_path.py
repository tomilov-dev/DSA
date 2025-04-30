class Solution:
    def min_cost(
        self,
        grid: list[list[int]],
    ) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[10**6] * (n + 1) for _ in range(n + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = grid[i][j]

        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if i == j == 1:
                    continue
                dp[i][j] += min(
                    dp[i][j - 1],
                    dp[i - 1][j],
                    dp[i - 1][j - 1],
                )
        return dp[m][n]


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3],
    ]
    print(Solution().min_cost(grid))
