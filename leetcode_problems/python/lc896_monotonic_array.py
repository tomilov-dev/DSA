class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) <= 2:
            return True

        prev = nums[0]
        index = 1
        while index < len(nums) - 1 and nums[index] == prev:
            index += 1

        if index == len(nums):
            return True

        direct = nums[index] - prev
        prev = nums[index]
        for index in range(index + 1, len(nums)):
            num = nums[index]
            if direct < 0:
                if num <= prev:
                    prev = num
                    continue
                else:
                    return False
            else:
                if num >= prev:
                    prev = num
                    continue
                else:
                    return False

        return True


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1, 1, 2, 4, 5]
    print(Solution().isMonotonic(nums))
