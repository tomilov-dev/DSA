MIN = -(10**9)


class SolutionRecursive:
    def maxScore(self, grid: list[list[int]]) -> int:
        def rec(i: int, j: int) -> int:
            if i >= m - 1 and j >= n - 1:
                return MIN

            score = MIN
            v = grid[i][j]
            if i + 1 < m:
                c = grid[i + 1][j] - v
                score = max(score, c, c + rec(i + 1, j))
            if j + 1 < n:
                c = grid[i][j + 1] - v
                score = max(score, c, c + rec(i, j + 1))
            return score

        m = len(grid)
        n = len(grid[0])
        best = MIN
        for i in range(m):
            for j in range(n):
                best = max(best, rec(i, j))
        return best


class SolutionTopDown:
    def maxScore(self, grid: list[list[int]]) -> int:
        def rec(i: int, j: int) -> int:
            if i >= m - 1 and j >= n - 1:
                return MIN

            key = (i, j)
            if key not in mem:
                score = MIN
                v = grid[i][j]
                if i + 1 < m:
                    c = grid[i + 1][j] - v
                    score = max(score, c, c + rec(i + 1, j))
                if j + 1 < n:
                    c = grid[i][j + 1] - v
                    score = max(score, c, c + rec(i, j + 1))
                mem[key] = score
            return mem[key]

        m = len(grid)
        n = len(grid[0])
        mem = dict()
        best = MIN
        for i in range(m):
            for j in range(n):
                best = max(best, rec(i, j))
        return best


class SolutionBottomUp:
    def maxScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[MIN] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = 0
        total = MIN
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                v = grid[i - 1][j - 1]
                if i - 2 >= 0:
                    score = v - grid[i - 2][j - 1]
                    dp[i][j] = max(
                        dp[i][j],
                        score,
                        score + dp[i - 1][j],
                    )
                    total = max(total, dp[i][j])
                if j - 2 >= 0:
                    score = v - grid[i - 1][j - 2]
                    dp[i][j] = max(
                        dp[i][j],
                        score,
                        score + dp[i][j - 1],
                    )
                    total = max(total, dp[i][j])
        return total


class SolutionBottomUpOptimized:
    def maxScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[MIN] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = 0
        total = MIN
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                v = grid[i - 1][j - 1]
                if i - 2 >= 0:
                    score = v - grid[i - 2][j - 1]
                    dp[i][j] = max(
                        dp[i][j],
                        score,
                        score + dp[i - 1][j],
                    )
                    total = max(total, dp[i][j])
                if j - 2 >= 0:
                    score = v - grid[i - 1][j - 2]
                    dp[i][j] = max(
                        dp[i][j],
                        score,
                        score + dp[i][j - 1],
                    )
                    total = max(total, dp[i][j])
        return total


if __name__ == "__main__":
    grid = [
        [9, 5, 7, 3],
        [8, 9, 6, 1],
        [6, 7, 14, 3],
        [2, 5, 3, 1],
    ]
    grid = [
        [4, 3, 2],
        [3, 2, 1],
    ]
    # sol = SolutionRecursive()
    # sol = SolutionTopDown()
    sol = SolutionBottomUp()
    print(sol.maxScore(grid))
