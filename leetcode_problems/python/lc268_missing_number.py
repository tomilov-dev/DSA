class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        index = 0
        for num in nums:
            if num != index:
                return index
            index += 1

        return index


if __name__ == "__main__":
    nums = [0, 1]
    print(Solution().missingNumber(nums))
