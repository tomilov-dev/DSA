class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxi = 2
        cur = 2
        n = len(nums)
        for i in range(2, n):
            if nums[i - 2] + nums[i - 1] == nums[i]:
                cur += 1
                maxi = max(maxi, cur)
            else:
                cur = 2
        return maxi


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 2, 3, 5, 1]
    nums = [5, 2, 7, 9, 16]
    nums = [1000000000, 1000000000, 1000000000]
    print(Solution().longestSubarray(nums))
