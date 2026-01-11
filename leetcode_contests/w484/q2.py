from collections import defaultdict


class Solution:
    def centeredSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            seen = set()
            s = 0
            for j in range(i, n):
                s += nums[j]
                seen.add(nums[j])
                if s in seen:
                    total += 1
        return total


class SolutionOptimized:
    def centeredSubarrays(self, nums: list[int]) -> int:
        s = 0
        sums = defaultdict(int)
        total = 0
        for x in nums:
            s += x
            sums[s] += 1
            total += sums[s]
        return total


if __name__ == "__main__":
    nums = [-1, 1, 0]
    # nums = [2, -3]
    print(SolutionOptimized().centeredSubarrays(nums))
