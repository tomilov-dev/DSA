class Solution:
    def longestAlternatingSubarray(
        self,
        nums: list[int],
        threshold: int,
    ) -> int:
        p1 = 0
        p2 = 0
        maxi = 0
        while p1 < len(nums) and p2 < len(nums):
            while p1 < len(nums) and (nums[p1] % 2 != 0 or nums[p1] > threshold):
                p1 += 1

            p2 = p1
            while (
                p2 < len(nums)
                and nums[p2] <= threshold
                and (p2 == p1 or nums[p2] % 2 != nums[p2 - 1] % 2)
            ):
                p2 += 1

            maxi = max(maxi, p2 - p1)
            p1 = p2

        return maxi


if __name__ == "__main__":
    nums = [3, 2, 5, 4]
    threshold = 5

    nums = [1, 2]
    threshold = 2

    nums = [2, 3, 4, 5]
    threshold = 4
    print(Solution().longestAlternatingSubarray(nums, threshold))
