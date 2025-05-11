class SolutionBottomUp:
    def numberOfPaths(
        self,
        m: int,
        n: int,
    ) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


class SolutionBottomUpOptimized:
    def numberOfPaths(
        self,
        m: int,
        n: int,
    ) -> int:
        dp = [1] * n
        for i in range(m - 1):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]


class SolutionCombinatorics:
    def numberOfPaths(
        self,
        m: int,
        n: int,
    ) -> int:
        path = 1
        for i in range(n, (m + n - 1)):
            path *= i
            path //= i - n + 1
        return path


if __name__ == "__main__":
    m = 3
    n = 3
    print(SolutionBottomUp().numberOfPaths(m, n))
    print(SolutionBottomUpOptimized().numberOfPaths(m, n))
    print(SolutionCombinatorics().numberOfPaths(m, n))
