class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        map = dict()
        for num in nums:
            map[num] = map.get(num, 0) + 1

        while original in map:
            original *= 2

        return original


if __name__ == "__main__":
    nums = [5, 3, 6, 1, 12]
    original = 3

    print(Solution().findFinalValue(nums, original))
