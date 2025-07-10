class SolutionRecursive:
    def nthTribonacci(self, n: int) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1
            return rec(i - 1) + rec(i - 2) + rec(i - 3)

        return rec(n)


class SolutionTopDown:
    def nthTribonacci(self, n: int) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1

            if i not in mem:
                mem[i] = rec(i - 1) + rec(i - 2) + rec(i - 3)
            return mem[i]

        mem = {}
        return rec(n)


class SolutionBottomUp:
    def nthTribonacci(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]


class SolutionBottomUpOptimized:
    def nthTribonacci(self, n: int) -> int:
        n1 = 0
        n2 = 1
        n3 = 1
        for i in range(3, n + 1):
            n4 = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = n4
        return n3


if __name__ == "__main__":
    n = 10
    print(SolutionRecursive().nthTribonacci(n))
    print(SolutionTopDown().nthTribonacci(n))
    print(SolutionBottomUp().nthTribonacci(n))
    print(SolutionBottomUpOptimized().nthTribonacci(n))
