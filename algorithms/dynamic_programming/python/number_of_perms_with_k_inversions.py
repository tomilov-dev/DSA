class SolutionRecursive:
    def countPermWithkInversions(
        self,
        n: int,
        k: int,
    ) -> int:
        def rec(n: int, k: int) -> int:
            if n == 0:
                return 0
            if k == 0:
                return 1

            res = 0
            for i in range(min(k, n - 1) + 1):
                res += rec(n - 1, k - i)
            return res

        return rec(n, k)


class SolutionTopDown:
    def countPermWithkInversions(
        self,
        n: int,
        k: int,
    ) -> int:
        def rec(n: int, k: int) -> int:
            if n == 0:
                return 0
            if k == 0:
                return 1

            key = (n, k)
            if key not in mem:
                res = 0
                for i in range(min(k, n - 1) + 1):
                    res += rec(n - 1, k - i)
                mem[key] = res
            return mem[key]

        mem = dict()
        return rec(n, k)


class SolutionBottomUp:
    def countPermWithkInversions(
        self,
        n: int,
        k: int,
    ) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for z in range(min(j, i - 1) + 1):
                    dp[i][j] += dp[i - 1][j - z]

        return dp[n][k]


class SolutionBottomUpOptimized:
    def countPermWithkInversions(
        self,
        n: int,
        k: int,
    ) -> int:
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            ndp = [0] * (k + 1)
            ndp[0] = 1
            for j in range(1, k + 1):
                for z in range(min(j, i - 1) + 1):
                    ndp[j] += dp[j - z]
            dp = ndp
        return dp[k]


if __name__ == "__main__":
    n = 4
    k = 1
    print(SolutionRecursive().countPermWithkInversions(n, k))
    print(SolutionTopDown().countPermWithkInversions(n, k))
    print(SolutionBottomUp().countPermWithkInversions(n, k))
    print(SolutionBottomUpOptimized().countPermWithkInversions(n, k))
