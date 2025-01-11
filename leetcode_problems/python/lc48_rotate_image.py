class Solution:
    def rotate(
        self,
        matrix: list[list[int]],
    ) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        ## transpone the matrix by swapping i,j -> j,i
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        ## transpone the matrix clockwise by swapping rows elements
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


if __name__ == "__main__":
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
    ]
    Solution().rotate(matrix)
    print(matrix)
