"""
Given an m x n binary matrix mat, return the number of special positions in mat.
A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    141 ms, 16.8 MB

    Mean time = 0.04524 ms
    Min time  = 0.04356 ms
    """

    @repeater()
    def run(self, matrix: list[list[int]]) -> int:
        count = 0
        for row_index in range(len(matrix)):
            row = matrix[row_index]
            check = sum(row)
            if check == 1:
                index = matrix[row_index].index(1)
                check = sum(map(lambda x: x[index], matrix))
                if check == 1:
                    count += 1

        return count


class Solution2(object):
    """
    149 ms, 16.7 MB

    Mean time = 1.29977 ms
    Min time  = 1.28867 ms
    """

    @repeater()
    def run(self, matrix: list[list[int]]) -> int:
        rows = [0 for _ in range(len(matrix))]
        cols = [0 for _ in range(len(matrix[0]))]

        for i in range(len(rows)):
            for j in range(len(cols)):
                if matrix[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        count = 0
        for i in range(len(rows)):
            for j in range(len(cols)):
                if matrix[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1

        return count


if __name__ == "__main__":
    matrix = [[random.randint(0, 1) for _ in range(50)] for _ in range(50)]

    sol1 = Solution1()
    sol2 = Solution2()

    sol1.run(matrix)
    sol2.run(matrix)
