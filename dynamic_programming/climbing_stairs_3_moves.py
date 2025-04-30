class Solution:
    def countWays(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(2, n):
            dp[i + 1] = dp[i] + dp[i - 1] + dp[i - 2]
        return dp[n]


class SolutionOptimized:
    def countWays(self, n: int) -> int:
        n1 = 1
        n2 = 1
        n3 = 2
        for _ in range(2, n):
            cur = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = cur
        return n3


class SolutionTopDown:
    def countWays(self, n: int) -> int:
        def backtrack(i: int) -> int:
            if i not in mem:
                mem[i] = backtrack(i - 1) + backtrack(i - 2) + backtrack(i - 3)
            return mem[i]

        mem = {0: 1, 1: 1, 2: 2}
        return backtrack(n)


if __name__ == "__main__":
    n = 19
    print(Solution().countWays(n))
    print(SolutionOptimized().countWays(n))
    print(SolutionTopDown().countWays(n))
