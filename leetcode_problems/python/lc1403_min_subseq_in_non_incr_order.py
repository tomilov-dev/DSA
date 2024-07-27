class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)

        lsum = 0
        rsum = sum(nums)
        index = 0

        while index < len(nums) and lsum <= rsum:
            lsum += nums[index]
            rsum -= nums[index]
            index += 1

        return nums[:index]


if __name__ == "__main__":
    nums = [4, 3, 10, 9, 8]
    print(Solution().minSubsequence(nums))
