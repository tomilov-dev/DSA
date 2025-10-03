class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1] + 2
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
        return dp[0][n - 1]
