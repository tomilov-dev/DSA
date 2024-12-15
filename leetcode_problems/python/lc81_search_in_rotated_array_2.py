class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        return target in nums


class Solution2:
    def search(self, nums: list[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True

            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] == nums[mid]:
                    low += 1
                if nums[high] == nums[mid]:
                    high -= 1

        return False


if __name__ == "__main__":
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0

    nums = [1, 0, 1, 1, 1]
    target = 0

    nums = [2, 2, 2, 3, 2, 2, 2]
    target = 3

    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
    target = 2

    print(Solution().search(nums, target))
