class Solution:
    def findChampion(
        self,
        grid: list[list[int]],
    ) -> int:
        msum = len(grid[0]) - 1
        for i in range(len(grid)):
            rsum = sum(grid[i])
            if rsum == msum:
                return i

        raise ValueError()


if __name__ == "__main__":
    grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
    print(Solution().findChampion(grid))
