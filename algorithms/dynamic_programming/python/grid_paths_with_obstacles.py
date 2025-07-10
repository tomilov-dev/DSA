class SolutionRecursive:
    def numberOfPaths(self, grid: list[list[int]]) -> int:
        def rec(i: int, j: int) -> int:
            if i == 1 and j == 1:
                return 1
            if i <= 0 or j <= 0:
                return 0
            if grid[i - 1][j - 1] == 1:
                return 0
            return rec(i - 1, j) + rec(i, j - 1)

        m = len(grid)
        n = len(grid[0])
        return rec(m, n)


class SolutionTopDown:
    def numberOfPaths(self, grid: list[list[int]]) -> int:
        def rec(i: int, j: int) -> int:
            if i == 1 and j == 1:
                return 1
            if i <= 0 or j <= 0:
                return 0
            if grid[i - 1][j - 1] == 1:
                return 0
            key = (i, j)
            if key not in mem:
                mem[key] = rec(i - 1, j) + rec(i, j - 1)
            return mem[key]

        m = len(grid)
        n = len(grid[0])
        mem = dict()
        return rec(m, n)


class SolutionBottomUp:
    def numberOfPaths(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = int(grid[0][0] == 0)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == j == 1:
                    continue
                if grid[i - 1][j - 1] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


class SolutionBottomUpOptimized:
    def numberOfPaths(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        ndp[1] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == j == 1:
                    continue
                if grid[i - 1][j - 1] == 1:
                    continue
                ndp[j] = dp[j] + ndp[j - 1]
            dp, ndp = ndp, dp
        return dp[n]


if __name__ == "__main__":
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    # print(SolutionBottomUpOptimized().numberOfPaths(grid))
    print(SolutionRecursive().numberOfPaths(grid))
    print(SolutionTopDown().numberOfPaths(grid))
    print(SolutionBottomUp().numberOfPaths(grid))
    print(SolutionBottomUpOptimized().numberOfPaths(grid))
