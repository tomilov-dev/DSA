class SolutionRecursive:
    def climbStairs(self, n: int) -> int:
        def rec(n: int) -> int:
            if n == 0 or n == 1:
                return 1
            return rec(n - 1) + rec(n - 2)

        return rec(n)


class SolutionTopDown:
    def climbStairs(self, n: int) -> int:
        def rec(n: int) -> int:
            if n not in mem:
                mem[n] = rec(n - 1) + rec(n - 2)
            return mem[n]

        mem = {0: 1, 1: 1}
        return rec(n)


class SolutionBottomUp:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class SolutionMemoryOptimized:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 1
        for _ in range(2, n + 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n2
