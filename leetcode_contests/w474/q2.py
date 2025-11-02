class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        pairs = [
            (nums[0], nums[1]),
            (nums[0], nums[-1]),
            (nums[0], nums[-2]),
            (nums[1], nums[-1]),
            (nums[1], nums[-2]),
            (nums[-1], nums[-2]),
        ]
        maxi = -(10**6)
        for x, y in pairs:
            for z in [-(10**5), 10**5]:
                maxi = max(maxi, x * y * z)
        return maxi


if __name__ == "__main__":
    nums = [-5, 7, 0]
    sol = Solution()
    print(sol.maxProduct(nums))
