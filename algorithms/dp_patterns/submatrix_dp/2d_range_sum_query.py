class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.prefix = self.build(matrix)

    def build(
        self,
        matrix: list[list[int]],
    ) -> list[list[int]]:
        n = len(matrix)
        m = len(matrix[0])

        prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prev_sum = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
                prefix[i][j] = matrix[i - 1][j - 1] + prev_sum

        return prefix

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int,
    ) -> int:
        row2 += 1
        col2 += 1
        return (
            self.prefix[row2][col2]
            - self.prefix[row1][col2]
            - self.prefix[row2][col1]
            + self.prefix[row1][col1]
        )
