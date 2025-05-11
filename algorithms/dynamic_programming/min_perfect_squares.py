import math


class SolutionBottomUp:
    def MinSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, math.floor(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


class SolutionTopDown:
    def MinSquares(self, n: int) -> int:
        def backtrack(i: int) -> int:
            if i not in mem:
                mem[i] = n
                for j in range(1, math.floor(math.sqrt(i)) + 1):
                    mem[i] = min(mem[i], backtrack(i - j * j) + 1)
            return mem[i]

        mem = {0: 0}
        return backtrack(n)


if __name__ == "__main__":
    n = 100
    print(SolutionBottomUp().MinSquares(n))
    print(SolutionTopDown().MinSquares(n))
