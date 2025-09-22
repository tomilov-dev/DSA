class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        nmin = min(nums)
        nmax = max(nums)
        return (nmax - nmin) * k
