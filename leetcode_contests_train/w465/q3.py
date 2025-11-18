import math


class SolutionBruteForce:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        maxwin = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] & nums[j] == 0:
                    maxwin = max(maxwin, nums[i] * nums[j])
        return maxwin


class SolutionBottomUp:
    def maxProduct(self, nums: list[int]) -> int:
        k = max(nums).bit_length()
        mask = 1 << k
        dp = [0] * mask
        for num in nums:
            dp[num] = num

        for i in range(mask):
            if dp[i]:
                continue
            for j in range(k):
                if i & (1 << j):
                    if dp[i ^ (1 << j)] > dp[i]:
                        dp[i] = dp[i ^ (1 << j)]

        return max(num * dp[(mask - 1) ^ num] for num in nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(SolutionBottomUp().maxProduct(nums))
