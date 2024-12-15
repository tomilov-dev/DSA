class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        memo = set()
        for num in nums:
            if num in memo:
                return True
            memo.add(num)

        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums))
