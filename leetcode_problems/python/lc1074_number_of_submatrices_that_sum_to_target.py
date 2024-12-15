class Solution:
    def dfs(
        self,
        matrix: list[list[int]],
        target: int,
    ) -> None:
        pass

    def numSubmatrixSumTarget(
        self,
        matrix: list[list[int]],
        target: int,
    ) -> int:
        self.count = 0

        return self.count


if __name__ == "__main__":
    matrix = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ]
    target = 0
    print(Solution().numSubmatrixSumTarget(matrix, target))
