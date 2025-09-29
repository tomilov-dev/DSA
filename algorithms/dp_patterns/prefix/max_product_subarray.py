class SolutionBottomUp:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, n):
            if nums[i] >= 0:
                # Отслеживаем, когда nums[i] >= 0 - тогда мы смотрим по макс. числу (желательно положительное)
                max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i])
                min_dp[i] = min(nums[i], min_dp[i - 1] * nums[i])
            else:
                # Отслеживаем, когда nums[i] < 0 - тогда мы смотрим по мин. числу (желательно отрицательное)
                max_dp[i] = max(nums[i], min_dp[i - 1] * nums[i])
                min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i])

        return max(max_dp)
