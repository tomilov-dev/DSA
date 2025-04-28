class Solution:
    def nthTribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(2, n):
            dp[i + 1] = dp[i] + dp[i - 1] + dp[i - 2]
        return dp[n]


class SolutionOptimized:
    def nthTribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        n1 = 0
        n2 = 1
        n3 = 1
        for _ in range(2, n):
            cur = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = cur
        return n3


if __name__ == "__main__":
    n = 15
    print(Solution().nthTribonacci(n))
    print(SolutionOptimized().nthTribonacci(n))
