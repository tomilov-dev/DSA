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


class Solution2:
    def missingNumber(self, nums: list[int]) -> int:
        current_sum = sum(nums)
        target_sum = len(nums) * (len(nums) + 1) // 2
        return target_sum - current_sum


if __name__ == "__main__":
    nums = [0, 1]
    nums = [3, 0, 1, 4]
    # print(Solution().missingNumber(nums))
    print(Solution2().missingNumber(nums))
