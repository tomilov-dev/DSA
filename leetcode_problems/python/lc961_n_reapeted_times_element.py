class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        map = dict()
        target = len(nums) // 2

        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num] == target:
                return num

        return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 3]
    print(Solution().repeatedNTimes(nums))
