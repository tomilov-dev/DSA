class Solution:
    def modifiedMatrix(
        self,
        matrix: list[list[int]],
    ) -> list[list[int]]:
        cols = [float("-inf")] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cols[j] = max(cols[j], matrix[i][j])

        answer = matrix[:]
        for i in range(len(answer)):
            for j in range(len(answer[0])):
                if answer[i][j] == -1:
                    answer[i][j] = cols[j]

        return answer


if __name__ == "__main__":
    matrix = [
        [1, 2, -1],
        [4, -1, 6],
        [7, 8, 9],
    ]
    print(Solution().modifiedMatrix(matrix))
