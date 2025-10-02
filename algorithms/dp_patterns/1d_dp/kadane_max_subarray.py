class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


class SolutionKadane:
    def maxSubArray(self, nums: list[int]) -> int:
        prev = nums[0]
        max_sum = prev
        for num in nums[1:]:
            prev = max(prev + num, num)
            max_sum = max(max_sum, prev)
        return max_sum
