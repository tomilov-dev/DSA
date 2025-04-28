class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n == 0:
            return 0

        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n):
            dp[i + 1] = dp[i] + dp[i - 1]
        return dp[n]


class SolutionOptimized:
    def nthFibonacci(self, n: int) -> int:
        if n == 0:
            return 0

        n1 = 0
        n2 = 1
        for _ in range(1, n):
            cur = n2 + n1
            n1 = n2
            n2 = cur
        return cur


if __name__ == "__main__":
    n = 5
    print(Solution().nthFibonacci(n))
    print(SolutionOptimized().nthFibonacci(n))
