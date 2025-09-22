class Solution:
    def evenNumberBitwiseORs(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            if num % 2 == 0:
                xor |= num
        return xor


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print(Solution().evenNumberBitwiseORs(nums))
