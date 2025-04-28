class Solution:
    def countWays(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            dp[i + 1] = dp[i] + dp[i - 1]
        return dp[n]


class SolutionOptimized:
    def countWays(self, n: int) -> int:
        n1 = 1
        n2 = 1
        for i in range(1, n):
            cur = n1 + n2
            n1 = n2
            n2 = cur
        return n2


if __name__ == "__main__":
    n = 4
    print(Solution().countWays(n))
    print(SolutionOptimized().countWays(n))
