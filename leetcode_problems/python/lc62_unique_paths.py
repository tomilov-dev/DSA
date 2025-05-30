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


if __name__ == "__main__":
    m = 3
    n = 7
    print(Solution().uniquePaths(m, n))
