class SolutionRecursive:
    def nCr(self, n: int, r: int) -> int:
        def rec(i: int, k: int) -> int:
            if k > i:
                return 0
            if k <= 0:
                return 1
            if i == k:
                return 1
            return self.nCr(i - 1, k) + self.nCr(i - 1, k - 1)

        return rec(n, r)


class SolutionTopDown:
    def nCr(self, n: int, r: int) -> int:
        def rec(i: int, k: int) -> int:
            if k > i:
                return 0
            if k <= 0:
                return 1
            if i == k:
                return 1
            if i not in mem:
                mem[i] = self.nCr(i - 1, k) + self.nCr(i - 1, k - 1)
            return mem[i]

        mem = {}
        return rec(n, r)


class SolutionBottomUp:
    def nCr(self, n: int, r: int) -> int:
        if r > n:
            return 0

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][i] = 1
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, r + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
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
        if r > n:
            return 0

        dp = [0] * (r + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(min(i, r), 0, -1):
                dp[j] = dp[j] + dp[j - 1]

        return dp[r]


if __name__ == "__main__":
    n = 5
    r = 2
    print(SolutionRecursive().nCr(n, r))
    print(SolutionTopDown().nCr(n, r))
    print(SolutionBottomUp().nCr(n, r))
    print(SolutionBottomUpOptimized().nCr(n, r))
