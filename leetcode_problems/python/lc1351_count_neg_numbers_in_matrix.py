class Solution:
    def bs_fneg(self, array: list[int]) -> int:
        lo = 0
        hi = len(array) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if array[mid] < 0:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def countNegatives(
        self,
        grid: list[list[int]],
    ) -> int:
        lrows = [len(row) for row in grid]
        count = 0
        for i in range(len(grid)):
            index = self.bs_fneg(grid[i])
            if index == 0:
                count += sum(lrows[i:])
                break

            else:
                count += lrows[index] - index

        return count


if __name__ == "__main__":
    grid = [
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3],
    ]
    print(Solution().countNegatives(grid))
