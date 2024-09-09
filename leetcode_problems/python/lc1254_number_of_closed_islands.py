class Solution:
    def fill(self, grid: list[list[int]], i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 0:
            return 0

        grid[i][j] = 1
        return (
            1
            + self.fill(grid, i + 1, j)
            + self.fill(grid, i, j + 1)
            + self.fill(grid, i - 1, j)
            + self.fill(grid, i, j - 1)
        )

    def closedIsland(self, grid: list[list[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i * j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
                    self.fill(grid, i, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.fill(grid, i, j) > 0:
                    res += 1

        return res


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]

    grid = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
    ]

    grid = [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]

    grid = [
        [0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1],
    ]

    print(Solution().closedIsland(grid))
