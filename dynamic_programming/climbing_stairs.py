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


class SolutionTopDown:
    def countWays(self, n: int) -> int:
        def backtrack(i: int) -> int:
            if i not in mem:
                mem[i] = backtrack(i - 1) + backtrack(i - 2)
            return mem[i]

        mem = {0: 1, 1: 1}
        return backtrack(n)


if __name__ == "__main__":
    n = 17
    print(Solution().countWays(n))
    print(SolutionOptimized().countWays(n))
    print(SolutionTopDown().countWays(n))
