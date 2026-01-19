from collections import defaultdict


class Solution:
    def minOperations(
        self,
        nums: list[int],
        target: list[int],
    ) -> int:
        mp = defaultdict(int)
        for i, x in enumerate(nums):
            if x != target[i]:
                mp[x] += 1
        return len(mp)


if __name__ == "__main__":
    print(Solution().minOperations(nums=[7, 3, 7], target=[5, 5, 9]))
