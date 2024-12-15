class Solution:
    def is_good(
        self,
        array: list[int],
        index: int,
    ) -> bool:
        return array[index] > array[-1]

    def findMin(
        self,
        nums: list[int],
    ) -> int:
        low = -1
        high = len(nums) - 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if self.is_good(nums, mid):
                low = mid
            else:
                high = mid
        return nums[high]


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(Solution().findMin(nums))
