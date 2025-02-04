from collections import deque


def inbound(grid: list[list[str]], i: int, j: int) -> bool:
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


class SolutionDFS:
    def dfs(self, i: int, j: int) -> None:
        if not inbound(self.grid, i, j):
            return None
        if self.grid[i][j] == "0" or self.used[i][j] == 1:
            return None

        self.used[i][j] = 1
        self.dfs(i, j + 1)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i - 1, j)

    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        self.used = [[0] * len(grid[i]) for i in range(len(grid))]

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and self.used[i][j] == 0:
                    res += 1
                    self.dfs(i, j)

        return res


class SolutionBFS:
    def numIslands(self, grid: list[list[str]]) -> int:
        res = 0
        used = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and used[i][j] == 0:
                    res += 1
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        if not inbound(grid, x, y):
                            continue
                        if grid[x][y] == "0" or used[x][y] == 1:
                            continue

                        used[x][y] = 1
                        q.append((x, y + 1))
                        q.append((x + 1, y))
                        q.append((x, y - 1))
                        q.append((x - 1, y))

        return res


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(SolutionBFS().numIslands(grid))
