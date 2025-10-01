class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        def is_same(points: list[tuple[int, int]]) -> bool:
            w = 0
            for x, y in points:
                w += int(grid[x][y] == "W")
            return w >= 3 or w <= 1

        return (
            is_same([(0, 0), (0, 1), (1, 0), (1, 1)])
            or is_same([(0, 1), (0, 2), (1, 1), (1, 2)])
            or is_same([(1, 0), (1, 1), (2, 0), (2, 1)])
            or is_same([(1, 1), (1, 2), (2, 1), (2, 2)])
        )


if __name__ == "__main__":
    grid = [
        ["B", "W", "B"],
        ["B", "W", "W"],
        ["B", "W", "B"],
    ]
    print(Solution().canMakeSquare(grid))
