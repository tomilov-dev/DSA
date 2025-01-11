class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return nums[low]


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    nums = [3, 3, 7, 7, 10, 11, 11]
    print(Solution().singleNonDuplicate(nums))
