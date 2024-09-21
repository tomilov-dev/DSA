class Solution:
    def findMaxConsecutiveOnes(
        self,
        nums: list[int],
    ) -> int:
        p1 = 0
        p2 = 0

        maxi = 0
        while p1 < len(nums):
            while p2 + 1 < len(nums) and nums[p2] == nums[p2 + 1]:
                p2 += 1

            if nums[p2] == 1:
                maxi = max(maxi, p2 - p1 + 1)

            p2 += 1
            p1 = p2

        return maxi


if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes(nums))
