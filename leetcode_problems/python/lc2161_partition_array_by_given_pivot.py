class Solution:
    def swap(
        self,
        nums: list[int],
        i: int,
        j: int,
    ) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    def pivotArray(
        self,
        nums: list[int],
        pivot: int,
    ) -> list[int]:
        j = 0
        for i in range(len(nums) - 1):
            if nums[i] <= pivot:
                self.swap(nums, i, j)
                j += 1

        self.swap(nums, -1, j)
        i = 0
        while i < j:
            if nums[i] == pivot:
                j -= 1
                self.swap(nums, i, j)
            i += 1

        return nums


if __name__ == "__main__":
    nums = [9, 12, 5, 10, 14, 3, 10]
    pivot = 10
    print(Solution().pivotArray(nums, pivot))
