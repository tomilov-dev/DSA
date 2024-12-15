class Solution:
    def sides(
        self,
        grid: list[list[int]],
        i: int,
        j: int,
    ) -> int:
        sides = 4
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            sides -= 1
        if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
            sides -= 1
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            sides -= 1
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            sides -= 1

        return sides

    def islandPerimeter(
        self,
        grid: list[list[int]],
    ) -> int:
        if not grid:
            return 0

        pm = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    pm += self.sides(grid, i, j)

        return pm


class Solution2:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter


if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
    ]
    print(Solution().islandPerimeter(grid))
