class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self._dp = self._build(matrix)

    def _build(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prev = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
                dp[i][j] = matrix[i - 1][j - 1] + prev
        return dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 += 1
        col2 += 1
        return (
            self._dp[row2][col2]
            - self._dp[row1][col2]
            - self._dp[row2][col1]
            + self._dp[row1][col1]
        )


if __name__ == "__main__":
    NumMatrix(
        [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
    )
