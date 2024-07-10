def unique_paths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i - 1][j]
            elif i == 0 and j > 0:
                dp[i][j] = dp[i][j - 1]

    return dp[m - 1][n - 1]


def unique_paths_obstacles(grid: list[list[int]]) -> int:
    m = len(grid)
    if not m:
        return 0

    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue

            if i > 0 and j > 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i - 1][j]
            elif i == 0 and j > 0:
                dp[i][j] = dp[i][j - 1]

    return dp[m - 1][n - 1]


def max_profit_path(grid: list[list[int]]) -> int:
    m = len(grid)
    if not m:
        return 0

    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            dp[i][j] = grid[i][j]
            if i > 0 and j > 0:
                dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])
            elif i > 0 and j == 0:
                dp[i][j] += dp[i - 1][j]
            elif i == 0 and j > 0:
                dp[i][j] += dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    obstacles_grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    profit_grid = [
        [1, 2, 2, 1],
        [3, 1, 1, 1],
        [4, 4, 2, 1],
    ]

    print(unique_paths(3, 4))
    print(unique_paths_obstacles(obstacles_grid))
    print(max_profit_path(profit_grid))
