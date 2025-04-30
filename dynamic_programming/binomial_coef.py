from pprint import pprint


class SolutionBottomUp:
    def nCr(self, n: int, r: int) -> int:
        if r > n:
            return 0

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1  # C(i, 0) = 1
            dp[i][i] = 1  # C(i, i) = 1

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[n][r]


class SolutionBottomUpGridOptimization:
    def nCr(self, n: int, r: int) -> int:
        if r > n:
            return 0

        dp = [[0] * (r + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1  # C(i, 0) = 1
            if i <= r:
                dp[i][i] = 1  # C(i, i) = 1

        for i in range(1, n + 1):
            for j in range(1, min(i, r) + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[n][r]


class SolutionBottomUpOptimized:
    def nCr(self, n: int, r: int) -> int:
        dp = [0] * (r + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(min(i, r), 0, -1):
                dp[j] = dp[j] + dp[j - 1]

        return dp[r]


if __name__ == "__main__":
    n = 5
    r = 2
    print(SolutionBottomUp().nCr(n, r))
    print(SolutionBottomUpGridOptimization().nCr(n, r))
