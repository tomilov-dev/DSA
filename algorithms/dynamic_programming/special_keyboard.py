class SolutionBottomUp:
    def optimalKeys(self, n: int) -> int:
        if n <= 6:
            return n

        dp = [0] * (n + 1)
        for i in range(1, 7):
            dp[i] = i

        for i in range(7, n + 1):
            for j in range(i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[n]


class SolutionBottomUpOptimized:
    def optimalKeys(self, n: int) -> int:
        if n <= 6:
            return n

        dp = [0] * (n + 1)
        for i in range(1, 7):
            dp[i] = i

        for i in range(7, n + 1):
            dp[i] = max(
                2 * dp[i - 3],
                3 * dp[i - 4],
                4 * dp[i - 5],
            )
        return dp[n]


if __name__ == "__main__":
    n = 4
    n = 7
    print(SolutionBottomUp().optimalKeys(n))
    print(SolutionBottomUpOptimized().optimalKeys(n))
