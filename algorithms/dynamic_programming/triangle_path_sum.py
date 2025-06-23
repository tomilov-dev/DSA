class SolutionRecursive:
    def minPathSum(
        self,
        triangle: list[list[int]],
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i >= len(triangle) or j >= len(triangle[i]):
                return 0
            return triangle[i][j] + min(
                rec(i + 1, j),
                rec(i + 1, j + 1),
            )

        return rec(0, 0)


class SolutionTopDown:
    def minPathSum(
        self,
        triangle: list[list[int]],
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i >= len(triangle) or j >= len(triangle[i]):
                return 0
            key = (i, j)
            if key not in mem:
                mem[key] = triangle[i][j] + min(
                    rec(i + 1, j),
                    rec(i + 1, j + 1),
                )
            return mem[key]

        mem = {}
        return rec(0, 0)


class SolutionBottomUp:
    def minPathSum(
        self,
        triangle: list[list[int]],
    ) -> int:
        n = len(triangle)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]


class SolutionBottomUpOptimized:
    def minPathSum(
        self,
        triangle: list[list[int]],
    ) -> int:
        n = len(triangle)
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(len(triangle[i])):
                ndp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
            dp, ndp = ndp, dp
        return dp[0]


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]
    print(SolutionRecursive().minPathSum(triangle))
    print(SolutionTopDown().minPathSum(triangle))
    print(SolutionBottomUp().minPathSum(triangle))
    print(SolutionBottomUpOptimized().minPathSum(triangle))
