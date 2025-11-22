class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1])
        min_r = 10**10
        for i in range(n - 1, -1, -1):
            if i + 1 < n and dp[i] > min_r:
                dp[i] = max(dp[i], dp[i + 1])
            min_r = min(min_r, nums[i])
        return dp
