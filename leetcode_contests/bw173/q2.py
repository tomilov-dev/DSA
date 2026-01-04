from collections import defaultdict


class Solution:
    def minLength(self, nums: list[int], k: int) -> int:
        MAX = 10**10
        i = 0
        mp = defaultdict(int)
        s = 0
        mini = MAX
        for j, num in enumerate(nums):
            mp[num] += 1
            if mp[num] == 1:
                s += num
            while s >= k:
                mini = min(mini, j - i + 1)
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    s -= nums[i]
                i += 1
        if mini == MAX:
            return -1
        return mini


if __name__ == "__main__":
    nums = [2, 2, 3, 1]
    k = 4

    # nums = [2, 2, 3, 3]
    # k = 6

    nums = [3, 2, 3, 4]
    k = 5

    nums = [5, 5, 4]
    k = 5

    nums = [6]
    k = 3
    print(Solution().minLength(nums, k))
