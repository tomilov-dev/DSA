class Solution:
    def is_good(self, val: int, target: int) -> bool:
        return val <= target

    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)
        while high - low > 1:
            mid = low + (high - low) // 2
            if self.is_good(nums[mid], target):
                low = mid
            else:
                high = mid

        return low if nums[low] == target else -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 3

    print(Solution().search(nums, target))
