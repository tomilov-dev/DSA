class SolutionRecursive:
    def numberOfPaths(
        self,
        m: int,
        n: int,
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i == 1 and j == 1:
                return 1
            if i <= 0 or j <= 0:
                return 0
            return rec(i - 1, j) + rec(i, j - 1)

        return rec(m, n)


class SolutionTopDown:
    def numberOfPaths(
        self,
        m: int,
        n: int,
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i == 1 and j == 1:
                return 1
            if i <= 0 or j <= 0:
                return 0

            key = (i, j)
            if key not in mem:
                mem[key] = rec(i - 1, j) + rec(i, j - 1)
            return mem[key]

        mem = dict()
        return rec(m, n)


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
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        ndp[1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                ndp[j] = dp[j] + ndp[j - 1]
            dp, ndp = ndp, dp
        return dp[n]


class SolutionBottomUpSuperOptimized:
    def numberOfPaths(
        self,
        m: int,
        n: int,
    ) -> int:
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
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

    print(SolutionRecursive().numberOfPaths(m, n))
    print(SolutionTopDown().numberOfPaths(m, n))
    print(SolutionBottomUp().numberOfPaths(m, n))
    print(SolutionBottomUpOptimized().numberOfPaths(m, n))
    print(SolutionBottomUpSuperOptimized().numberOfPaths(m, n))
    print(SolutionCombinatorics().numberOfPaths(m, n))
