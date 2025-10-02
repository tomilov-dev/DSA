import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class SolutionOptimal:
    def lengthOfLIS(self, nums: list[int]) -> int:
        seq = []
        for num in nums:
            idx = bisect.bisect_left(seq, num)
            if idx == len(seq):
                seq.append(num)
            else:
                seq[idx] = num
        return len(seq)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(SolutionOptimal().lengthOfLIS(nums))
