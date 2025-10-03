MAX = 10**9


class Solution:
    def minPathSum(
        self,
        grid: list[list[int]],
    ) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[MAX] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]


class SolutionOptimal:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [0] * n
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = grid[0][0]
                else:
                    top = prev[j] if i > 0 else MAX
                    left = curr[j - 1] if j > 0 else MAX
                    curr[j] = grid[i][j] + min(top, left)
            prev = curr
        return prev[n - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))
