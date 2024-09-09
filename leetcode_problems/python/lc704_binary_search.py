class Solution:
    def search(self, nums: list[int], target: int) -> int:
        bot = 0
        top = len(nums)
        while bot < top:
            mid = bot + (top - bot) // 2
            if nums[mid] < target:
                bot = mid + 1
            elif nums[mid] > target:
                top = mid
            else:
                return mid


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 12

    print(Solution().search(nums, target))
