class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))
