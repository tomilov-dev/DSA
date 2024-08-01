class Solution:
    def maxIncreaseKeepingSkyline(
        self,
        grid: list[list[int]],
    ) -> int:
        maxrow = [0 for _ in range(len(grid))]
        maxcol = [0 for _ in range(len(grid[0]))]

        for ri in range(len(grid)):
            for ci in range(len(grid[ri])):
                value = grid[ri][ci]
                maxrow[ri] = max(maxrow[ri], value)
                maxcol[ci] = max(maxcol[ci], value)

        growth = 0
        for ri in range(len(grid)):
            for ci in range(len(grid[ri])):
                growth += min(maxrow[ri], maxcol[ci]) - grid[ri][ci]

        return growth


if __name__ == "__main__":
    grid = [
        [3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0],
    ]
    print(Solution().maxIncreaseKeepingSkyline(grid))
