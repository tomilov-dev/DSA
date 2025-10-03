class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m][n]


class SolutionOptimal:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n
        for _ in range(1, m):
            curr = [0] * n
            for j in range(n):
                left = curr[j - 1] if j > 0 else 0
                curr[j] = prev[j] + left
            prev = curr
        return prev[n - 1]
