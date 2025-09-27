class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        def surface(i: int, j: int, l: int, r: int) -> int:
            maxi = grid[i][j]
            if l >= n or l < 0 or r >= n or r < 0:
                return maxi
            return max(maxi - grid[l][r], 0)

        def topbot(i: int, j: int) -> int:
            if grid[i][j] > 0:
                return 2
            return 0

        n = len(grid)
        c = 0
        for i in range(n):
            for j in range(n):
                c += topbot(i, j)
                sides = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for ls, rs in sides:
                    c += surface(i, j, i + ls, j + rs)
        return c


if __name__ == "__main__":
    grid = [[1, 2], [3, 4]]
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    print(Solution().surfaceArea(grid))
