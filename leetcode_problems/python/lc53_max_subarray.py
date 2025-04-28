class SolutionDPBottomUp:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


class SolutionDPTopDown:
    def maxSubArray(self, nums: list[int]) -> int:
        def dp(i: int) -> int:
            if i in memo:
                return memo[i]

            if i == 0:
                memo[i] = nums[0]
                return memo[i]

            memo[i] = max(dp(i - 1) + nums[i], nums[i])
            return memo[i]

        n = len(nums)
        memo = {}
        max_sum = -10000000000
        for i in range(n):
            max_sum = max(max_sum, dp(i))

        return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(SolutionDPBottomUp().maxSubArray(nums))
