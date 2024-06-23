"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells 
(i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, 
we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
"""
import math


class Solution1(object):
    def mean(
        self,
        row: int,
        col: int,
        matrix: list[list[int]],
    ) -> int:
        sum = 0
        indexes = set()

        for irow in range(max(0, row - 1), min(row + 2, self.maxrow)):
            for icol in range(max(0, col - 1), min(col + 2, self.maxcol)):
                indexes.add((irow, icol))

        for index in indexes:
            sum += matrix[index[0]][index[1]]

        return math.floor(sum / len(indexes))

    def run(
        self,
        matrix: list[list[int]],
    ) -> list[list[int]]:
        self.maxrow = len(matrix)
        self.maxcol = len(matrix[0])

        smoother = [[None for _ in range(self.maxcol)] for _ in range(self.maxrow)]

        for row in range(self.maxrow):
            for col in range(self.maxcol):
                smoother[row][col] = self.mean(row, col, matrix)

        return smoother


if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]

    sol1 = Solution1()

    print(sol1.run(matrix))
