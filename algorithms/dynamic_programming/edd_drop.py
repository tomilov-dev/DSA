MIN = 10**6


class SolutionRecursive:
    def eggDrop(self, n: int, k: int) -> int:
        def rec(ni: int, ki: int) -> int:
            if ki == 1 or ki == 0:
                return ki
            if ni == 1:
                return ki

            mini = MIN
            for i in range(1, ki + 1):
                sub = 1 + max(
                    rec(ni - 1, i - 1),
                    rec(ni, ki - i),
                )
                mini = min(mini, sub)
            return mini

        return rec(n, k)


class SolutionTopDown:
    def eggDrop(self, n: int, k: int) -> int:
        def rec(ni: int, ki: int) -> int:
            if ki == 1 or ki == 0:
                return ki
            if ni == 1:
                return ki

            key = (ni, ki)
            if key not in mem:
                mini = MIN
                for i in range(1, ki + 1):
                    sub = 1 + max(
                        rec(ni - 1, i - 1),
                        rec(ni, ki - i),
                    )
                    mini = min(mini, sub)
                mem[key] = mini
            return mem[key]

        mem = {}
        return rec(n, k)


class SolutionBottomUp:
    def eggDrop(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for j in range(k + 1):
            dp[1][j] = j

        for i in range(1, n + 1):
            dp[i][0] = 0
            dp[i][1] = 1

        for i in range(2, n + 1):
            for j in range(2, k + 1):
                dp[i][j] = MIN
                for x in range(1, j + 1):
                    res = 1 + max(
                        dp[i - 1][x - 1],  # яйцо разбилось
                        dp[i][j - x],  # яйцо не разбилось
                    )
                    dp[i][j] = min(dp[i][j], res)

        return dp[n][k]


if __name__ == "__main__":
    n = 2
    k = 36
    # print(SolutionRecursive().eggDrop(n, k))
    print(SolutionTopDown().eggDrop(n, k))
    print(SolutionBottomUp().eggDrop(n, k))
