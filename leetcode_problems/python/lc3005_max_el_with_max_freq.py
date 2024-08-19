class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        map = dict()
        for num in nums:
            map[num] = map.get(num, 0) + 1

        maxfreq = max(map.values())
        count = 0
        for num, freq in map.items():
            if freq == maxfreq:
                count += freq

        return count


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1, 4]
    print(Solution().maxFrequencyElements(nums))
