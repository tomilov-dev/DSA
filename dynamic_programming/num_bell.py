class SolutionBottomUp:
    def bellNumber(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][i - 1]
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

        return dp[n][0]


class SolutionBottomUpOptimized:
    def bellNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            prev = dp[:]
            dp[0] = prev[i - 1]
            for j in range(1, i + 1):
                dp[j] = prev[j - 1] + dp[j - 1]

        return dp[0]


if __name__ == "__main__":
    n = 4
    print(SolutionBottomUp().bellNumber(n))
    print(SolutionBottomUpOptimized().bellNumber(n))
