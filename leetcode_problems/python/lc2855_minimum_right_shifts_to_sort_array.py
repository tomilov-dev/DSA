class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        index = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                if index != 0:
                    return -1
                index = i
        if index != 0 and nums[0] < nums[-1]:
            return -1
        return n - index if index != 0 else 0


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    nums = [1, 3, 5]
    nums = [2, 1, 4]
    print(Solution().minimumRightShifts(nums))
