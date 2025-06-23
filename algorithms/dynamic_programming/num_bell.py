class SolutionRecursive:
    def bellNumber(self, n: int) -> int:
        def rec(i: int, k: int) -> int:
            if i == 0 and k == 0:
                return 1
            if i == 0 or k == 0:
                return 0
            if i == k:
                return 1
            if k == 1:
                return 1
            return k * rec(i - 1, k) + rec(i - 1, k - 1)

        res = 0
        for k in range(1, n + 1):
            res += rec(n, k)
        return res


class SolutionTopDown:
    def bellNumber(self, n: int) -> int:
        def rec(i: int, k: int) -> int:
            if i == 0 and k == 0:
                return 1
            if i == 0 or k == 0:
                return 0
            if i == k:
                return 1
            if k == 1:
                return 1

            key = (i, k)
            if key not in mem:
                mem[key] = k * rec(i - 1, k) + rec(i - 1, k - 1)
            return mem[key]

        mem = {}
        res = 0
        for k in range(1, n + 1):
            res += rec(n, k)
        return res


class SolutionBottomUp:
    def bellNumber(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][i - 1]
            for j in range(1, i + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
        return dp[n][0]


class SolutionBottomUpOptimized:
    def bellNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        dp[0] = 1
        ndp = [0] * (n + 1)
        for i in range(1, n + 1):
            ndp[0] = dp[i - 1]
            for j in range(1, i + 1):
                ndp[j] = ndp[j - 1] + dp[j - 1]
            dp, ndp = ndp, dp
        return dp[0]


if __name__ == "__main__":
    n = 4
    print(SolutionRecursive().bellNumber(n))
    print(SolutionTopDown().bellNumber(n))
    print(SolutionBottomUp().bellNumber(n))
    print(SolutionBottomUpOptimized().bellNumber(n))
