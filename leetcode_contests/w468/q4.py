class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = []
        for i in range(n):
            xmin = nums[i]
            xmax = nums[i]
            for j in range(i + 1, n):
                xmin = min(xmin, nums[j])
                xmax = max(xmax, nums[j])
                ans.append(xmax - xmin)
        ans.sort(reverse=True)
        return sum(ans[:k])


if __name__ == "__main__":
    nums = [1, 3, 2]
    k = 2

    nums = [4, 2, 5, 1]
    k = 3

    nums = [18, 36, 6]
    k = 3
    print(Solution().maxTotalValue(nums, k))
