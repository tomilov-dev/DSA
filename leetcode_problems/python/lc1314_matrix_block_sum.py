class Solution:
    def build_prefix(
        self,
        mat: list[list[int]],
    ) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0])

        prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prev_sum = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
                prefix[i][j] = mat[i - 1][j - 1] + prev_sum

        return prefix

    def sum_region(
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

    def matrixBlockSum(
        self,
        mat: list[list[int]],
        k: int,
    ) -> list[list[int]]:
        block_sum = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        self.prefix = self.build_prefix(mat)
        for i in range(len(mat)):
            for j in range(len(mat)):
                row1 = max(0, i - k)
                col1 = max(0, j - k)
                row2 = min(i + k, len(mat) - 1)
                col2 = min(j + k, len(mat[0]) - 1)
                block_sum[i][j] = self.sum_region(row1, col1, row2, col2)

        return block_sum


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(Solution().matrixBlockSum(mat, k))
