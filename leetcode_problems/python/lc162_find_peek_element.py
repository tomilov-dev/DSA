class Solution:
    def is_peek(
        self,
        nums: list[int],
        i: int,
    ) -> bool:
        if i == 0:
            return nums[i] > nums[i + 1]
        elif i == len(nums) - 1:
            return nums[i] > nums[i - 1]
        else:
            return nums[i - 1] < nums[i] and nums[i + 1] < nums[i]

    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.is_peek(nums, mid):
                return mid
            elif nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]
    nums = [1, 2, 3, 1]
    print(Solution().findPeakElement(nums))
