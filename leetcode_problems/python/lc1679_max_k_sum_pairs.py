"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    508 ms, 30.6 MB

    Mean time = 7.25506 ms
    Min time  = 7.09525 ms
    """

    @repeater()
    def run(self, nums: list[int], k: int) -> int:
        count = 0
        mapper = {}
        for num in nums:
            if num in mapper:
                mapper[num] += 1
            else:
                mapper[num] = 1

        for num in nums:
            other_num = k - num

            if num == other_num:
                if mapper[num] >= 2:
                    count += 1
                    mapper[num] -= 2

            else:
                if mapper.get(other_num, 0) > 0 and mapper[num] > 0:
                    count += 1
                    mapper[other_num] -= 1
                    mapper[num] -= 1

        return count


class Solution2(object):
    """
    524 ms, 29.6 MB

    Mean time = 5.94576 ms
    Min time  = 5.75458 ms
    """

    @repeater()
    def run(self, nums: list[int], k: int) -> int:
        count = 0
        nums.sort()

        left, right = 0, len(nums) - 1
        while left < right and nums[left] < k:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1

        return count


if __name__ == "__main__":
    # nums = [3, 1, 3, 4, 3]
    nums = [random.randint(0, 100) for _ in range(10000)]
    k = random.randint(0, 100)

    sol1 = Solution1()
    sol2 = Solution2()

    # print(sol1.run(nums, k))
    print(sol2.run(nums, k))
