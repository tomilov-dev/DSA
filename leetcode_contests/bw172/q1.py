import math


class SolutionTLE:
    def minOperations(self, nums: list[int]) -> int:
        mp = dict()
        for i, num in enumerate(nums):
            mp[num] = mp.get(num, 0) + 1
        i = 0
        while i < len(nums):
            distinct = True
            for num, fq in mp.items():
                if fq > 1:
                    distinct = False
            if distinct:
                break
            for j in range(i, min(i + 3, len(nums))):
                mp[nums[j]] -= 1
                i += 1
        return math.ceil(i / 3)


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        last = -1
        mp = dict()
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            mp[num] = mp.get(num, 0) + 1
            if mp[num] > 1:
                last = i
                break
        if last == -1:
            return 0
        return math.ceil((i + 1) / 3)


if __name__ == "__main__":
    nums = [3, 8, 3, 6, 5, 8]
    # nums = [2, 2]
    # nums = [4, 3, 5, 1, 2]
    # nums = [87, 15, 26, 32, 32, 18]
    print(Solution().minOperations(nums))
