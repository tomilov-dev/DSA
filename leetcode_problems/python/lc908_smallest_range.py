class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        xmin = min(nums) + k
        xmax = max(nums) - k
        return xmax - xmin if xmax >= xmin else 0


if __name__ == "__main__":
    nums = [0, 10]
    k = 2
    print(Solution().smallestRangeI(nums, k))
