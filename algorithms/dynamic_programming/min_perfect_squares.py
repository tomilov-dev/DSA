import math


class SolutionRecursive:
    def MinSquares(self, n: int) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 0

            mini = 10**6
            for j in range(1, math.floor(math.sqrt(i))):
                mini = min(mini, 1 + rec(i - j * j))
            return mini

        return rec(n)


class SolutionTopDown:
    def MinSquares(self, n: int) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 0

            if i not in mem:
                mem[i] = 10**6
                for j in range(1, math.floor(math.sqrt(i)) + 1):
                    mem[i] = min(mem[i], 1 + rec(i - j * j))
            return mem[i]

        mem = {}
        return rec(n)


class SolutionBottomUp:
    def MinSquares(self, n: int) -> int:
        dp = [10**6] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, math.floor(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], 1 + dp[i - j * j])
        return dp[n]


if __name__ == "__main__":
    n = 100
    # print(SolutionRecursive().MinSquares(n))
    print(SolutionTopDown().MinSquares(n))
    print(SolutionBottomUp().MinSquares(n))
