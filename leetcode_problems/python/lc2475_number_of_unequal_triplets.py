class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        map = dict()
        for num in nums:
            map[num] = map.get(num, 0) + 1

        total = 0
        left = 0
        right = len(nums)

        for num in map:
            right -= map[num]
            total += left * map[num] * right
            left += map[num]

        return total


if __name__ == "__main__":
    nums = [4, 4, 2, 4, 3]
    print(Solution().unequalTriplets(nums))
