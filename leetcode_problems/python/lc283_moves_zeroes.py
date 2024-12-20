"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

import random
from time_measure import repeater


class Solution1(object):
    """
    150 ms, 17.9 MB

    Mean time = 3.61501 ms
    Min time  = 3.54809 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> None:
        pointer = 0
        zero_point = len(nums)
        while pointer < zero_point:
            if nums[pointer] == 0:
                nums.append(nums.pop(pointer))
                zero_point -= 1
            else:
                pointer += 1

        return None


class Solution2(object):
    """
    155 ms, 17.9 MB

    Mean time = 5.27219 ms
    Min time  = 5.11746 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> None:
        walker = 0
        for runner in range(len(nums)):
            if nums[runner] != 0 and nums[walker] == 0:
                nums[walker], nums[runner] = nums[runner], nums[walker]

            if nums[walker] != 0:
                walker += 1

        return None


class Solution3:
    def swap(
        self,
        arr: list[int],
        p1: int,
        p2: int,
    ) -> None:
        arr[p1], arr[p2] = arr[p2], arr[p1]

    def moveZeroes(self, nums: list[int]) -> None:
        p1 = 0
        p2 = 0
        while p1 < len(nums) and p2 < len(nums):
            while p2 < len(nums) and nums[p2] == 0:
                p2 += 1

            if p1 < len(nums) and p2 < len(nums):
                self.swap(nums, p1, p2)
                p2 += 1
                p1 += 1


if __name__ == "__main__":
    nums = [random.randint(0, 10) for _ in range(10000)]

    sol1 = Solution1()
    sol2 = Solution2()

    sol1.run(nums)
    sol2.run(nums)
