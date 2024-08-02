class Solution:
    def countKDifference(
        self,
        nums: list[int],
        k: int,
    ) -> int:
        map = dict()
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1

        count = 0
        for index in range(len(nums)):
            num = nums[index]
            count += map.get(num + k, 0)
            count += map.get(num - k, 0)
            map[num] -= 1

        return count


if __name__ == "__main__":
    nums = [1, 2, 2, 1]
    k = 1

    print(Solution().countKDifference(nums, k))
