class Solution:
    def partitionArray(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        mp = dict()
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
            if mp[num] > n // k:
                return False
        return True
