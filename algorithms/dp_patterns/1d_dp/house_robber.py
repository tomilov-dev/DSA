class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
        return dp[n]


class SolutionOptimal:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        n1 = 0
        n2 = nums[0]
        for i in range(2, n + 1):
            n3 = max(nums[i - 1] + n1, n2)
            n1 = n2
            n2 = n3
        return n2
