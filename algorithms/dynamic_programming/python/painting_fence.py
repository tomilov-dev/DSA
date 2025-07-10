class SolutionRecursive:
    def countWays(
        self,
        n: int,
        k: int,
    ) -> int:
        def rec(i: int, k: int) -> int:
            if i == n - 1:
                return k
            if i == n - 2:
                return k * k
            return rec(i + 1, k) * (k - 1) + rec(i + 2, k) * (k - 1)

        return rec(0, k)


class SolutionTopDown:
    def countWays(
        self,
        n: int,
        k: int,
    ) -> int:
        def rec(i: int, k: int) -> int:
            if i == n - 1:
                return k
            if i == n - 2:
                return k * k
            key = (i, k)
            if key not in mem:
                mem[key] = rec(i + 1, k) * (k - 1) + rec(i + 2, k) * (k - 1)
            return mem[key]

        mem = {}
        return rec(0, k)


class SolutionBottomUp:
    def countWays(
        self,
        n: int,
        k: int,
    ) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
        return dp[n]


class SolutionBottomUpOptimized:
    def countWays(
        self,
        n: int,
        k: int,
    ) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k

        n1 = k
        n2 = k * k
        for i in range(3, n + 1):
            cur = n1 * (k - 1) + n2 * (k - 1)
            n1 = n2
            n2 = cur
        return n2


if __name__ == "__main__":
    n = 2
    k = 4
    print(SolutionRecursive().countWays(n, k))
    print(SolutionTopDown().countWays(n, k))
    print(SolutionBottomUp().countWays(n, k))
    print(SolutionBottomUpOptimized().countWays(n, k))
