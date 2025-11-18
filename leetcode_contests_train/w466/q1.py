class Solution:
    def minOperations(self, nums: list[int]) -> int:
        prev = nums[0]
        for num in nums[1:]:
            if prev != num:
                return 1
            prev = num
        return 0


if __name__ == "__main__":
    nums = [1, 2]
    print(Solution().minOperations(nums))
