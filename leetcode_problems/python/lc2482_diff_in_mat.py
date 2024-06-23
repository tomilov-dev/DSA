"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    TLE

    Mean time = 17.51764 ms
    Min time  = 16.64267 ms
    """

    @repeater()
    def run(self, matrix: list[list[int]]) -> list[int]:
        new_matrix = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                onesRowi = len([v for v in matrix[i] if v == 1])
                onesColj = len([v for v in map(lambda x: x[j], matrix) if v == 1])
                zerosRowi = len([v for v in matrix[i] if v == 0])
                zerosColj = len([v for v in map(lambda x: x[j], matrix) if v == 0])

                new_matrix[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

        return new_matrix


class Solution2(object):
    """
    1410 ms, 52.9 MB

    Mean time = 0.57952 ms
    Min time  = 0.56104 ms
    """

    @repeater()
    def run(self, matrix: list[list[int]]) -> list[int]:
        row_count = len(matrix)
        col_count = len(matrix[0])

        ones_rows = [sum(matrix[i]) for i in range(row_count)]
        ones_cols = [sum(map(lambda x: x[j], matrix)) for j in range(col_count)]

        new_matrix = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                onesRowi = ones_rows[i]
                zerosRowi = row_count - onesRowi

                onesColj = ones_cols[j]
                zerosColj = col_count - onesColj

                new_matrix[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

        return new_matrix


class Solution3(object):
    @repeater()
    def run(self, matrix: list[list[int]]) -> list[list[int]]:
        row = [0] * len(matrix)
        col = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row[i] += matrix[i][j]
                col[j] += matrix[i][j]

        diff = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diff[i][j] = 2 * row[i] + 2 * col[j] - len(matrix) - len(matrix[0])

        return diff


if __name__ == "__main__":
    matrix = [[random.randint(0, 1) for _ in range(20)] for _ in range(20)]

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    sol1.run(matrix)
    sol2.run(matrix)
    sol3.run(matrix)
