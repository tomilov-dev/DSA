class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]


class Solution2:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]
        for i in range(1, n):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[n]


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
