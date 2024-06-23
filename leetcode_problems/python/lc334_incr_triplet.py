"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
"""
import math
from time_measure import repeater


class Solution1(object):
    """
    892 ms, 16.7 MB

    Mean time = 0.21333 ms
    Min time  = 0.19991 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> bool:
        v1, v2 = math.inf, math.inf

        for index in range(len(nums)):
            value = nums[index]

            if value <= v1:
                v1 = value
            elif value <= v2:
                v2 = value
            else:
                return True

        return False


if __name__ == "__main__":
    nums = list(range(1000)[::-1])

    sol1 = Solution1()

    print(sol1.run(nums))
