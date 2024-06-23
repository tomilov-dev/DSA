"""
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    150 ms, 17.7 MB

    Mean time = 1.14470 ms
    Min time  = 1.12663 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] * nums[1]) - (nums[-2] * nums[-1])


class Solution2(object):
    """
    158 ms, 17.7 MB

    Mean time = 3.32151 ms
    Min time  = 3.28185 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        a, b, c, d = 0, 0, float("inf"), float("inf")
        for num in nums:
            if b <= num:
                if a <= num:
                    temp = b
                    b = a
                    a = num
                    num = temp
                else:
                    temp = b
                    b = num
                    num = temp

            if num == 0:
                continue

            if d >= num:
                if c >= num:
                    d = c
                    c = num
                else:
                    d = num

        return (a * b) - (c * d)


class Solution3(object):
    """
    154 ms, 17.7 MB

    Mean time = 4.96512 ms
    Min time  = 4.92728 ms
    """

    @repeater()
    def run(self, nums: list[int]) -> int:
        a, b, c, d = 0, 0, float("inf"), float("inf")
        for num in nums:
            if a < num or b < num:
                b = max(a, b)
                a = num

            if c > num or d > num:
                d = min(c, d)
                c = num

        return (a * b) - (c * d)


if __name__ == "__main__":
    nums = list(range(1, 10000))
    random.shuffle(nums)

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    print(sol1.run(nums))
    print(sol2.run(nums))
    print(sol3.run(nums))
