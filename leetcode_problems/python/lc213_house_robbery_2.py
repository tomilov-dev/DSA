class Solution:
    def dp(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = max(dp[1], nums[1])
        for i in range(2, n):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[n]

    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp1 = self.dp(nums[:-1])
        dp2 = self.dp(nums[1:])
        return max(dp1, dp2)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
