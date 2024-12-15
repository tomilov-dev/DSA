"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
"""


class Solution(object):
    """
    Binary search solution.

    35 ms, 16.1 MB
    """

    def run(self, x: int) -> int:
        if x == 0:
            return 0

        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1

        return last


class Solution2:
    def is_good(self, value: int, target: int) -> bool:
        return value * value <= target

    def mySqrt(self, x: int) -> int:
        low = 1
        high = x + 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if self.is_good(mid, x):
                low = mid
            else:
                high = mid

        return low


if __name__ == "__main__":
    x = 8

    sol = Solution2()
    print(sol.mySqrt(x))
