MIN = -(10**9)


class SolutionOptimalKadane:
    def maxSumSubmatrix(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        max_sum = MIN
        for top in range(m):
            col_sums = [0] * n
            for bottom in range(top, m):
                for col in range(n):
                    col_sums[col] += matrix[bottom][col]

                current_sum = 0
                max_current = MIN
                for col_sum in col_sums:
                    current_sum = max(col_sum, current_sum + col_sum)
                    max_current = max(max_current, current_sum)
                max_sum = max(max_sum, max_current)

        return max_sum


if __name__ == "__main__":
    matrix = [
        [1, 2, -1],
        [-3, 4, 5],
        [2, -1, 2],
    ]
    matrix = [
        [-1, -2],
        [-3, -4],
    ]
    matrix = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9],
    ]
    print(SolutionOptimalKadane().maxSumSubmatrix(matrix))
