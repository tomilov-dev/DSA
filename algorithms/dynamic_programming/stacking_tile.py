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
            if height < 0 or size <= 0:
                return 0

            c = 0
            # min(k, height) - не асимптотическая оптимизация
            for i in range(0, min(k, height) + 1):
                c += rec(height - i, size - 1)
            return c

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
            if height < 0 or size <= 0:
                return 0

            key = (height, size)
            if key not in mem:
                c = 0
                # min(k, height) - не асимптотическая оптимизация
                for i in range(0, min(k, height) + 1):
                    c += rec(height - i, size - 1)
                mem[key] = c
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
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # Нулевая строка обязана быть из 1
        for j in range(m + 1):
            dp[0][j] = 1

        for h in range(1, n + 1):
            for s in range(1, m + 1):
                for i in range(0, min(k, h) + 1):
                    # i = 0 => dp[h][s - 1] - инициализация
                    dp[h][s] += dp[h - i][s - 1]
        return dp[h][s]


class SolutionBottomUpOptimized:
    def stack(
        self,
        n: int,
        m: int,
        k: int,
    ) -> int:
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        for s in range(1, m + 1):
            dp[0] = 1
            for h in range(1, n + 1):
                for i in range(0, min(k, h) + 1):
                    ndp[h] += dp[h - i]
            dp, ndp = ndp, dp
        return dp[s]


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
