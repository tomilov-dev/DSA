class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue

            dp[i] = dp[i + 1]
            if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]


class SolutionOptimal:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        n1 = 1
        n2 = 0
        for i in range(n - 1, -1, -1):
            n3 = 0
            if s[i] != "0":
                n3 = n1
                if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                    n3 += n2
            n1 = n3
            n2 = n1
        return n1
