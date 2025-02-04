class Solution:
    def getMaximumGold(
        self,
        grid: list[list[int]],
    ) -> int:
        def correct(i: int, j: int) -> bool:
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def backtrack(
            i: int,
            j: int,
            cur: int,
        ) -> None:
            nonlocal maxi

            if not correct(i, j) or used[i][j] or not grid[i][j]:
                maxi = max(maxi, cur)
                return None

            used[i][j] = True
            cur += grid[i][j]
            paths = [
                (+0, -1),
                (-1, +0),
                (+0, +1),
                (+1, +0),
            ]
            for ix, iy in paths:
                backtrack(i + ix, j + iy, cur)
            used[i][j] = False

        maxi = 0
        used = [[False] * len(grid[0]) for i in range(len(grid))]
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] != 0:
                    backtrack(x, y, 0)
        return maxi


if __name__ == "__main__":
    grid = [
        [0, 6, 0],
        [5, 8, 7],
        [0, 9, 0],
    ]

    grid = [
        [1, 0, 7],
        [2, 0, 6],
        [3, 4, 5],
        [0, 3, 0],
        [9, 0, 20],
    ]
    print(Solution().getMaximumGold(grid))
