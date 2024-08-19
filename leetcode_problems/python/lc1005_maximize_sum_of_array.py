class Solution:
    def largestSumAfterKNegations(
        self,
        nums: list[int],
        k: int,
    ) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        index = 0
        while k > 0 and index < len(nums):
            if nums[index] < 0:
                nums[index] = -nums[index]
                k -= 1
            index += 1

        if k > 0:
            min_index = 0
            for index in range(len(nums)):
                if nums[index] < nums[min_index]:
                    min_index = index
            nums[min_index] = nums[min_index] * (-1) ** k

        return sum(nums)


if __name__ == "__main__":
    nums = [-2, 5, 0, 2, -2]
    k = 3

    print(Solution().largestSumAfterKNegations(nums, k))
