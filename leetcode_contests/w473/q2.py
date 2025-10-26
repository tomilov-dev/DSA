class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        sn = nums[:]
        sn.sort(key=lambda x: x**2)

        start = 0
        end = len(nums) - 1
        score = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                score += sn[end] ** 2
                end -= 1
            else:
                score -= sn[start] ** 2
                start += 1
        return score


if __name__ == "__main__":
    nums = [1, 2, 3]
    # nums = [1, -1, 2, -2, 3, -3]
    # nums = [12, -4]
    sol = Solution()
    print(sol.maxAlternatingSum(nums))
