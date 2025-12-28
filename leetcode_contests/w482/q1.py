class Solution:
    def maximumScore(self, nums: list[int]) -> int:
        MIN = -(10**10)

        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        suff = [float("inf")] * (n + 1)
        for i in range(n - 1, 0, -1):
            suff[i] = min(nums[i], suff[i + 1])

        maxi = MIN
        for i in range(n - 1):
            maxi = max(maxi, pref[i + 1] - suff[i + 1])
        return maxi


if __name__ == "__main__":
    nums = [10, -1, 3, -4, -5]
    nums = [-7, -5, 3]
    nums = [1, 1]
    print(Solution().maximumScore(nums))
