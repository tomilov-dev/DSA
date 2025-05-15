class SolutionRecursive:
    def lucas(self, n: int) -> int:
        def rec(i: int):
            if i == 0:
                return 2
            if i == 1:
                return 1
            return rec(i - 1) + rec(i - 2)

        return rec(n)


class SolutionTopDown:
    def lucas(self, n: int) -> int:
        def rec(i: int):
            if i == 0:
                return 2
            if i == 1:
                return 1
            if i not in mem:
                mem[i] = rec(i - 1) + rec(i - 2)
            return mem[i]

        mem = {}
        return rec(n)


class SolutionBottomUp:
    def lucas(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 2
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class SolutionBottomUpOptimized:
    def lucas(self, n: int) -> int:
        n1 = 2
        n2 = 1
        for i in range(2, n + 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n2


if __name__ == "__main__":
    n = 7
    print(SolutionRecursive().lucas(n))
    print(SolutionTopDown().lucas(n))
    print(SolutionBottomUp().lucas(n))
    print(SolutionBottomUpOptimized().lucas(n))
