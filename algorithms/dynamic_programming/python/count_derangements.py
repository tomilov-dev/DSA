class SolutionRecursive:
    def countDer(self, n: int):
        def rec(i: int) -> int:
            if i == 0:
                return 1
            if i == 1:
                return 0
            if i < 0:
                return 0
            return (i - 1) * (rec(i - 1) + rec(i - 2))

        return rec(n)


class SolutionTopDown:
    def countDer(self, n: int):
        def rec(i: int) -> int:
            if i == 0:
                return 1
            if i == 1:
                return 0
            if i < 0:
                return 0
            if i not in mem:
                mem[i] = (i - 1) * (rec(i - 1) + rec(i - 2))
            return mem[i]

        mem = dict()
        return rec(n)


class SolutionBottomUp:
    def countDer(self, n: int):
        dp = [0] * (n + 1)
        dp[0] = 1  # By condition
        dp[1] = 0  # By condition
        for i in range(2, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
        return dp[n]


class SolutionBottomUpOptimized:
    def countDer(self, n: int):
        n1 = 1
        n2 = 0
        for i in range(2, n + 1):
            cur = (i - 1) * (n1 + n2)
            n1 = n2
            n2 = cur
        return n2


if __name__ == "__main__":
    n = 11
    print(SolutionRecursive().countDer(n))
    print(SolutionTopDown().countDer(n))
    print(SolutionBottomUp().countDer(n))
    print(SolutionBottomUpOptimized().countDer(n))
