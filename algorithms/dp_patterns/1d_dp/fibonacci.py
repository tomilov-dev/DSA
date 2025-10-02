class Solution:
    def fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class SolutionOptimal:
    def fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        n1 = 0
        n2 = 1
        for _ in range(2, n + 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n2
