class Solution:
    def lucas(self, n: int) -> int:
        if n == 0:
            return 2
        elif n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 2
        dp[1] = 1
        for i in range(1, n):
            dp[i + 1] = (dp[i] + dp[i - 1]) % (10**9 + 7)
        return dp[n]


class SolutionOptimized:
    def lucas(self, n: int) -> int:
        if n == 0:
            return 2
        elif n == 1:
            return 1

        n1 = 2
        n2 = 1
        for i in range(1, n):
            cur = (n1 + n2) % (10**9 + 7)
            n1 = n2
            n2 = cur
        return n2


if __name__ == "__main__":
    n = 5
    print(Solution().lucas(n))
