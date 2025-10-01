class SolutionBottomUp:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        m = max(nums)
        count = [0] * (m + 1)
        for num in nums:
            count[num] += 1

        dp = [0] * (m + 1)
        dp[1] = count[1]
        for i in range(2, m + 1):
            dp[i] = max(i * count[i] + dp[i - 2], dp[i - 1])
        return dp[m]


if __name__ == "__main__":
    nums = [3, 4, 2]
    nums = [2, 2, 3, 3, 3, 4]
    sol = SolutionBottomUp()
    print(sol.deleteAndEarn(nums))
