import math


class Solution:
    def numberOfRoutes(self, grid: list[str], d: int) -> int:
        def end(i, j):
            key = (i, j)
            if key in endmem:
                return endmem[key]
            moves = 1
            for nj in range(max(0, j - d), min(m, j + d + 1)):
                if nj == j or grid[i][nj] != ".":
                    continue
                moves += 1
            endmem[key] = moves
            return moves

        def rec(i: int, j: int, stayed: bool):
            if not (0 <= i < n and 0 <= j < m):
                return 0
            if grid[i][j] != ".":
                return 0
            if i == 0:
                return end(i, j)
            key = (i, j, stayed)
            if key in mem:
                return mem[key]
            moves = 0

            if not stayed:
                for nj in range(max(0, j - d), min(m, j + d + 1)):
                    if nj == j or grid[i][nj] != ".":
                        continue
                    moves = (moves + rec(i, nj, True)) % MOD

            max_up = int((d2 - 1) ** 0.5) if d2 > 1 else 0
            for nj in range(max(0, j - max_up), min(m, j + max_up + 1)):
                if grid[i - 1][nj] != ".":
                    continue
                if 1 + (j - nj) ** 2 > d2:
                    continue
                moves = (moves + rec(i - 1, nj, False)) % MOD
            mem[key] = moves
            return moves

        def eucv(x1: int, y1: int, x2: int, y2: int, d: int) -> bool:
            key = (x1, y1, x2, y2)
            if key not in eucmem:
                eucmem[key] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= d
            return eucmem[key]

        MOD = 10**9 + 7
        mem = dict()
        endmem = dict()
        eucmem = dict()
        n = len(grid)
        m = len(grid[0])
        total = 0
        d2 = d * d
        for j in range(m):
            if grid[n - 1][j] == ".":
                total = (total + rec(n - 1, j, False)) % MOD
        return total


class SolutionBottomUp:
    def numberOfRoutes(self, grid: list[str], d: int) -> int:
        MOD = 10**9 + 7
        n = len(grid)
        m = len(grid[0])

        stay = [[[] for _ in range(m)] for _ in range(n)]
        up = [[[] for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] != ".":
                    continue
                for nj in range(m):
                    if nj != j and grid[i][nj] == "." and math.sqrt((j - nj) ** 2) <= d:
                        stay[i][j].append(nj)
                if i > 0:
                    for nj in range(m):
                        if (
                            grid[i - 1][nj] == "."
                            and math.sqrt((i - (i - 1)) ** 2 + (j - nj) ** 2) <= d
                        ):
                            up[i][j].append(nj)

        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
        for j in range(m):
            if grid[n - 1][j] == ".":
                dp[n - 1][j][0] = 1

        for i in range(n - 1, 0, -1):
            for j in range(m):
                for stayed in [0, 1]:
                    val = dp[i][j][stayed]
                    if val == 0:
                        continue
                    if not stayed:
                        for nj in stay[i][j]:
                            dp[i][nj][1] = (dp[i][nj][1] + val) % MOD
                    for nj in up[i][j]:
                        dp[i - 1][nj][0] = (dp[i - 1][nj][0] + val) % MOD

        total = 0
        for j in range(m):
            total = (total + dp[0][j][0] + dp[0][j][1]) % MOD
            if grid[0][j] == ".":
                for stayed in [0, 1]:
                    val = dp[0][j][stayed]
                    if val == 0:
                        continue
                    for nj in range(m):
                        if nj == j or grid[0][nj] != ".":
                            continue
                        if math.sqrt((j - nj) ** 2) <= d:
                            total = (total + val) % MOD
        return total


if __name__ == "__main__":
    grid = ["..", "#."]
    d = 1

    grid = [".#"]
    d = 1
    print(Solution().numberOfRoutes(grid, d))
