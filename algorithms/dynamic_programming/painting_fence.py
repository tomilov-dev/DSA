class SolutionBottomUpFirst:
    def countWays(
        self,
        n: int,
        k: int,
    ) -> int:
        dp = [0] * (n + 1)
        dp[1] = k
        for i in range(1, n):
            dp[i + 1] = dp[i] * (k - 1) + dp[i - 1] * (k - 1)
        return dp[n] + dp[n - 1]


class SolutionBottomUpCorrect:
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
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
        return dp[n]


class SolutionBottomUpFirstOptimized:
    def countWays(
        self,
        n: int,
        k: int,
    ) -> int:
        n1 = 0
        n2 = k
        for i in range(1, n):
            cur = n2 * (k - 1) + n1 * (k - 1)
            n1 = n2
            n2 = cur
        return n1 + n2


class SolutionBottomUpCorrectOptimized:
    def countWays(
        self,
        n: int,
        k: int,
    ) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        n1 = k
        n2 = k * k
        for i in range(3, n + 1):
            cur = n2 * (k - 1) + n1 * (k - 1)
            n1 = n2
            n2 = cur
        return n2


if __name__ == "__main__":
    n = 2
    k = 4
    print(SolutionBottomUpFirst().countWays(n, k))
    print(SolutionBottomUpCorrect().countWays(n, k))

    print(SolutionBottomUpFirstOptimized().countWays(n, k))
    print(SolutionBottomUpCorrectOptimized().countWays(n, k))
