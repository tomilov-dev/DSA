class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for cur_sum in range(target, num - 1, -1):
                dp[cur_sum] = dp[cur_sum] or dp[cur_sum - num]
        return dp[target]
