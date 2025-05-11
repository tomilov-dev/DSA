class SolutionRecursive:
    def stack(
        self,
        n: int,
        m: int,
        k: int,
    ) -> int:
        def rec(height: int, size: int) -> int:
            if height == 0:
                return 1
            if size == 0:
                return 0

            res = 0
            for comp_height in range(min(k, height) + 1):
                res += rec(height - comp_height, size - 1)

            return res

        return rec(n, m)


class SolutionTopDown:
    def stack(
        self,
        n: int,
        m: int,
        k: int,
    ) -> int:
        def rec(height: int, size: int) -> int:
            if height == 0:
                return 1
            if size == 0:
                return 0

            key = (height, size)
            if key not in mem:
                mem[key] = 0
                res = 0
                for comp_height in range(min(k, height) + 1):
                    res += rec(height - comp_height, size - 1)
                mem[key] = res
            return mem[key]

        mem = dict()
        return rec(n, m)


class SolutionBottomUp:
    def stack(
        self,
        n: int,
        m: int,
        k: int,
    ) -> int:
        # n - count of rows in stack (height)
        # m - count of cols in stack (width)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i][j - 1]
                for h in range(1, min(k, i) + 1):
                    dp[i][j] += dp[i - h][j - 1]

        return dp[n][m]


class SolutionBottomUpOptimized:
    def stack(
        self,
        n: int,
        m: int,
        k: int,
    ) -> int:
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        dp[0] = 1

        for j in range(1, m + 1):
            dp[0] = 1
            for i in range(1, n + 1):
                ndp[i] = dp[i]
                for h in range(1, min(k, i) + 1):
                    ndp[i] += dp[i - h]
            dp, ndp = ndp, dp

        return dp[n]


if __name__ == "__main__":
    n = 3
    m = 3
    k = 1

    n = 3
    m = 3
    k = 2
    print(SolutionRecursive().stack(n, m, k))
    print(SolutionTopDown().stack(n, m, k))
    print(SolutionBottomUp().stack(n, m, k))
    print(SolutionBottomUpOptimized().stack(n, m, k))
