class SolutionRecursive:
    def count(self, matrix: list[list[int]]) -> int:
        def rec(i: int, j: int) -> int:
            nonlocal max_side
            if i < 0 or j < 0 or not matrix[i][j]:
                return 0

            side = 1 + min(
                rec(i - 1, j - 1),
                rec(i - 1, j),
                rec(i, j - 1),
            )
            max_side = max(max_side, side)
            return side

        max_side = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                rec(i, j)
        return max_side


class SolutionTopDown:
    def count(self, matrix: list[list[int]]) -> int:
        def rec(i: int, j: int) -> int:
            nonlocal max_side
            if i < 0 or j < 0 or not matrix[i][j]:
                return 0

            key = (i, j)
            if key not in mem:
                mem[key] = 1 + min(
                    rec(i - 1, j - 1),
                    rec(i - 1, j),
                    rec(i, j - 1),
                )
                max_side = max(max_side, mem[key])
                return mem[key]
            return mem[key]

        max_side = 0
        mem = {}
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                rec(i, j)
        return max_side


class SolutionBottomUp:
    def count(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxi = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1],
                    )
                    maxi = max(maxi, dp[i][j])
        return maxi


class SolutionBottomUpOptimized:
    def count(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        maxi = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    ndp[j] = 1 + min(dp[j], ndp[j - 1], dp[j - 1])
                    maxi = max(maxi, ndp[j])
                else:
                    ndp[j] = 0
            dp, ndp = ndp, dp
        return maxi


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    print(SolutionRecursive().count(matrix))
    print(SolutionTopDown().count(matrix))
    print(SolutionBottomUp().count(matrix))
    print(SolutionBottomUpOptimized().count(matrix))
