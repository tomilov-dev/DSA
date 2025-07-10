class SolutionRecursive:
    def min_cost(
        self,
        grid: list[list[int]],
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= m or j >= n:
                return 10**6
            if i == 0 and j == 0:
                return grid[0][0]
            return grid[i][j] + min(
                rec(i - 1, j),
                rec(i, j - 1),
                rec(i - 1, j - 1),
            )

        m = len(grid)
        n = len(grid[0])
        return rec(m - 1, n - 1)


class SolutionTopDown:
    def min_cost(
        self,
        grid: list[list[int]],
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= m or j >= n:
                return 10**6
            if i == 0 and j == 0:
                return grid[0][0]
            key = (i, j)
            if key not in mem:
                mem[key] = grid[i][j] + min(
                    rec(i - 1, j),
                    rec(i, j - 1),
                    rec(i - 1, j - 1),
                )
            return mem[key]

        m = len(grid)
        n = len(grid[0])
        mem = {}
        return rec(m - 1, n - 1)


class SolutionBottomUp:
    def min_cost(
        self,
        grid: list[list[int]],
    ) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[10**6] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                dp[i][j] = grid[i - 1][j - 1] + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1],
                )
        return dp[m][n]


class SolutionBottomUpOptimized:
    def min_cost(
        self,
        grid: list[list[int]],
    ) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [10**6] * (n + 1)
        ndp = [10**6] * (n + 1)
        dp[1] = grid[0][0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                ndp[j] = grid[i - 1][j - 1] + min(
                    dp[j],
                    ndp[j - 1],
                    dp[j - 1],
                )
            dp, ndp = ndp, dp
        return dp[n]


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3],
    ]
    print(SolutionRecursive().min_cost(grid))
    print(SolutionTopDown().min_cost(grid))
    print(SolutionBottomUp().min_cost(grid))
    print(SolutionBottomUpOptimized().min_cost(grid))
