class SolutionRecursive:
    def nthFibonacci(self, n: int) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return 1
            return rec(i - 1) + rec(i - 2)

        return rec(n)


class SolutionTopDown:
    def nthFibonacci(self, n: int) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i not in mem:
                mem[i] = rec(i - 1) + rec(i - 2)
            return mem[i]

        mem = {}
        return rec(n)


class SolutionBottomUp:
    def nthFibonacci(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]


class SolutionBottomUpOptimized:
    def nthFibonacci(self, n: int) -> int:
        n1 = 0
        n2 = 1
        for i in range(2, n + 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n2


if __name__ == "__main__":
    n = 7
    print(SolutionRecursive().nthFibonacci(n))
    print(SolutionTopDown().nthFibonacci(n))
    print(SolutionBottomUp().nthFibonacci(n))
    print(SolutionBottomUpOptimized().nthFibonacci(n))
