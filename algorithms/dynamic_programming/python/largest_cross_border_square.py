class SolutionBruteForce:
    def largestSubsquare(
        self,
        matrix: list[list[str]],
    ) -> int:
        def isSquare(
            xi: int,
            yi: int,
            xj: int,
            yj: int,
        ) -> bool:
            for y in range(yi, yj + 1):
                if matrix[xi][y] != "X":
                    return False
                if matrix[xj][y] != "X":
                    return False

            for x in range(xi, xj + 1):
                if matrix[x][yi] != "X":
                    return False
                if matrix[x][yj] != "X":
                    return False

            return True

        m = len(matrix)
        n = len(matrix[0])
        maxi = 0
        for x in range(0, m):
            for y in range(0, n):
                kmax = min(m - x, n - y)
                for k in range(kmax):
                    if isSquare(x, y, x + k, y + k):
                        maxi = max(maxi, k + 1)
        return maxi


class SolutionBottomUp:
    def largestSubsquare(
        self,
        matrix: list[list[str]],
    ) -> int:
        def isSquare(
            xi: int,
            yi: int,
            xj: int,
            yj: int,
            t: int,
        ) -> bool:
            return (
                dp[xi][yj][0] == t
                and dp[xj][yi][1] == t
                and dp[xj][yj][0] == t
                and dp[xj][yj][1] == t
            )

        m = len(matrix)
        n = len(matrix[0])

        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        # x setup = X^2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "X":
                    dp[i][j][0] = 1 + dp[i][j - 1][0]
        # y setup = X^2
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[j - 1][i - 1] == "X":
                    dp[j][i][1] = 1 + dp[j - 1][i][1]

        maxi = 0
        for x in range(0, m):
            for y in range(0, n):
                kmax = min(m - x, n - y)
                for k in range(kmax):
                    if isSquare(x, y, x + k, y + k, k + 1):
                        maxi = max(maxi, k + 1)
        return maxi


if __name__ == "__main__":
    matrix = [
        ["X", "X", "X", "O"],
        ["X", "O", "X", "X"],
        ["X", "X", "X", "O"],
        ["X", "O", "X", "X"],
    ]

    # matrix = [
    #     ["X", "X"],
    #     ["X", "X"],
    # ]
    print(SolutionBruteForce().largestSubsquare(matrix))
    print(SolutionBottomUp().largestSubsquare(matrix))
