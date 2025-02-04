class Solution:
    def minimumDifference(
        self,
        nums: list[int],
        k: int,
    ) -> int:
        if k >= len(nums):
            return max(nums) - min(nums)

        nums.sort()
        p1 = 0
        p2 = k - 1
        mini = float("inf")
        while p1 < len(nums) and p2 < len(nums):
            mini = min(mini, nums[p2] - nums[p1])
            p1 += 1
            p2 += 1

        return int(mini)


if __name__ == "__main__":
    nums = [9, 4, 1, 7]
    k = 2
    print(Solution().minimumDifference(nums, k))
