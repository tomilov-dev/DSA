class Solution:
    def oddCells(
        self,
        m: int,
        n: int,
        indices: list[list[int]],
    ) -> int:
        rows = [0] * m
        cols = [0] * n

        for row, col in indices:
            rows[row] += 1
            cols[col] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                count += (rows[i] + cols[j]) % 2 != 0

        return count


if __name__ == "__main__":
    m = 2
    n = 2
    indices = [[1, 1], [0, 0]]

    m = 2
    n = 3
    indices = [[0, 1], [1, 1]]

    print(Solution().oddCells(m, n, indices))
