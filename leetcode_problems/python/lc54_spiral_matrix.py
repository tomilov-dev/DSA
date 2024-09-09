class Solution:
    def transpose_and_reverse(
        self,
        matrix: list[list[int]],
    ) -> list[list[int]]:
        return [list(row) for row in zip(*matrix)][::-1]

    def spiralOrder(
        self,
        matrix: list[list[int]],
    ) -> list[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix:
                matrix = self.transpose_and_reverse(matrix)
        return result


if __name__ == "__main__":
    matrix = [
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34],
    ]
    print(Solution().spiralOrder(matrix))
