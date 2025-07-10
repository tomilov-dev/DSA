MIN = -(10**6)


class SolutionRecursive:
    def count(
        self,
        n: int,
        x: int,
        y: int,
        arr1: list[int],
        arr2: list[int],
    ) -> int:
        def rec(i: int, x: int, y: int) -> int:
            if x < 0 or y < 0:
                return MIN
            if i >= len(arr1):
                return 0
            return max(
                arr1[i] + rec(i + 1, x - 1, y),
                arr2[i] + rec(i + 1, x, y - 1),
                rec(i + 1, x, y),
            )

        return rec(0, x, y)


class SolutionTopDown:
    def count(
        self,
        n: int,
        x: int,
        y: int,
        arr1: list[int],
        arr2: list[int],
    ) -> int:
        def rec(i: int, x: int, y: int) -> int:
            if x < 0 or y < 0:
                return MIN
            if i >= len(arr1):
                return 0
            key = (i, x, y)
            if key not in mem:
                mem[key] = max(
                    arr1[i] + rec(i + 1, x - 1, y),
                    arr2[i] + rec(i + 1, x, y - 1),
                    rec(i + 1, x, y),
                )
            return mem[key]

        mem = dict()
        return rec(0, x, y)


class SolutionBottomUp:
    def count(
        self,
        n: int,
        x: int,
        y: int,
        arr1: list[int],
        arr2: list[int],
    ) -> int:
        m = len(arr1)
        dp = [[[0] * (y + 1) for _ in range(x + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for xi in range(1, x + 1):
                for yi in range(1, y + 1):
                    dp[i][xi][yi] = max(
                        arr1[i - 1] + dp[i - 1][xi - 1][yi],
                        arr2[i - 1] + dp[i - 1][xi][yi - 1],
                        dp[i - 1][xi][yi],
                    )

        return dp[m][x][y]


class SolutionBottomUpOptimized:
    def count(
        self,
        n: int,
        x: int,
        y: int,
        arr1: list[int],
        arr2: list[int],
    ) -> int:
        m = len(arr1)
        dp = [[0] * (y + 1) for _ in range(x + 1)]
        ndp = [[0] * (y + 1) for _ in range(x + 1)]

        for i in range(1, m + 1):
            for xi in range(1, x + 1):
                for yi in range(1, y + 1):
                    ndp[xi][yi] = max(
                        arr1[i - 1] + dp[xi - 1][yi],
                        arr2[i - 1] + dp[xi][yi - 1],
                        dp[xi][yi],
                    )
            dp, ndp = ndp, dp

        return dp[x][y]


if __name__ == "__main__":
    n = 5
    x = 3
    y = 3
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 4, 3, 2, 1]
    print(SolutionRecursive().count(n, x, y, arr1, arr2))
    print(SolutionTopDown().count(n, x, y, arr1, arr2))
    print(SolutionBottomUp().count(n, x, y, arr1, arr2))
    print(SolutionBottomUpOptimized().count(n, x, y, arr1, arr2))
