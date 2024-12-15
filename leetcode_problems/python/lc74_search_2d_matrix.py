class Solution:
    def get_value(
        self,
        matrix: list[list[int]],
        index: int,
    ) -> int:
        return matrix[index // len(matrix[0])][index % len(matrix[0])]

    def is_good(
        self,
        value: int,
        target: int,
    ) -> bool:
        return value <= target

    def searchMatrix(
        self,
        matrix: list[list[int]],
        target: int,
    ) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0])

        while high - low > 1:
            mid = low + (high - low) // 2
            value = self.get_value(matrix, mid)
            if self.is_good(value, target):
                low = mid
            else:
                high = mid

        value = self.get_value(matrix, low)
        return value == target


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(Solution().searchMatrix(matrix, target))
