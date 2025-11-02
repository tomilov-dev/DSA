class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        mini = min(nums)
        maxi = max(nums)
        isin = set(nums)
        miss = []
        for x in range(mini, maxi + 1):
            if x not in isin:
                miss.append(x)
        return miss
