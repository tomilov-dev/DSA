class Solution:
    def findAllPossiblePaths(
        self,
        n: int,
        m: int,
        grid: list[list[int]],
    ) -> list[list[int]]:
        def rec(i: int, j: int) -> None:
            stack.append(grid[i][j])
            if i == m - 1 and j == n - 1:
                res.append(stack[:])

            if i + 1 < m:
                rec(i + 1, j)
            if j + 1 < n:
                rec(i, j + 1)
            stack.pop()

        m = len(grid)
        n = len(grid[0])
        stack = []
        res = []
        rec(0, 0)
        return res


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    print(
        Solution().findAllPossiblePaths(
            len(grid),
            len(grid[0]),
            grid,
        )
    )
