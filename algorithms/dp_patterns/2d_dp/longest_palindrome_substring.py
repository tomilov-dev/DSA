class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        for length in range(3, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    start = l
                    max_len = length

        return s[start : start + max_len]
