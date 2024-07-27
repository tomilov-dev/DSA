class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0

        ops = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]

            incr = num - prev
            incr = 0 if incr > 0 else abs(incr) + 1

            ops += incr
            prev = num + incr

        return ops


if __name__ == "__main__":
    nums = [1, 5, 2, 4, 1]
    print(Solution().minOperations(nums))
