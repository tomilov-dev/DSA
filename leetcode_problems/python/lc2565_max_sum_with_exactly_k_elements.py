class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        return k * max(nums) + (k * (k - 1)) // 2


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 3

    print(Solution().maximizeSum(nums, k))
