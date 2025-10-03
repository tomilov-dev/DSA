class Solution:
    def longestCommonSubstring(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_len


class SolutionOptimal:
    def longestCommonSubstring(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        prev = [0] * (n + 1)
        max_len = 0
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                    max_len = max(max_len, curr[j])
                else:
                    curr[j] = 0
            prev = curr
        return max_len
