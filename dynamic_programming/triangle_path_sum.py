class SolutionBottomUp:
    def minPathSum(
        self,
        triangle: list[list[int]],
    ) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            new_dp = triangle[i][:]
            for j in range(len(dp) - 1):
                new_dp[j] += min(dp[j], dp[j + 1])
            dp = new_dp
        return dp[0]


class SolutionBottomUpOptimized:
    def minPathSum(
        self,
        triangle: list[list[int]],
    ) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]


class SolutionTopDown:
    def minPathSum(
        self,
        triangle: list[list[int]],
    ) -> int:
        def backtrack(i: int, j: int) -> int:
            if i == len(triangle):
                return 0
            if (i, j) in mem:
                return mem[(i, j)]

            mem[(i, j)] = triangle[i][j] + min(
                backtrack(i + 1, j),
                backtrack(i + 1, j + 1),
            )
            return mem[(i, j)]

        mem = {}
        return backtrack(0, 0)


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]
    print(SolutionBottomUp().minPathSum(triangle))
    print(SolutionBottomUpOptimized().minPathSum(triangle))
    print(SolutionTopDown().minPathSum(triangle))
