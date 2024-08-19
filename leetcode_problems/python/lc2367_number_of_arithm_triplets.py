class Solution:
    def arithmeticTriplets(
        self,
        nums: list[int],
        diff: int,
    ) -> int:
        map = dict()
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1

        count = 0
        for num in nums:
            if map.get(num + diff) and map.get(num + diff * 2):
                count += 1

        return count


if __name__ == "__main__":
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3

    print(Solution().arithmeticTriplets(nums, diff))
