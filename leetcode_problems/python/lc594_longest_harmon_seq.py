class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        p1 = 0
        p2 = 0
        maxi = 0

        while p2 < len(nums):
            if nums[p2] - nums[p1] > 1:
                p1 += 1
            elif nums[p2] - nums[p1] == 1:
                maxi = max(maxi, p2 - p1 + 1)
                p2 += 1
            else:
                p2 += 1

        return maxi


if __name__ == "__main__":
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    # nums = [1, 1, 2, 2, 5, 2, 3, 7]
    print(Solution().findLHS(nums))
