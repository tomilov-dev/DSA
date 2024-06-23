"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
"""
import random
from time_measure import repeater


class Solution1(object):
    """
    TLE

    Mean time = 412.07793 ms
    Min time  = 401.44802 ms
    """

    @repeater()
    def run(self, height: list[int]) -> int:
        max_w = 0
        for p1 in range(len(height)):
            for p2 in range(p1 + 1, len(height)):
                hgt = min(height[p1], height[p2])
                wdt = p2 - p1
                max_w = max(max_w, hgt * wdt)

        return max_w


class Solution2(object):
    """
    528 ms, 30 mb

    Mean time = 1.06255 ms
    Min time  = 1.04911 ms
    """

    @repeater()
    def run(self, height: list[int]) -> int:
        max_w = 0
        p1 = 0
        p2 = len(height) - 1

        while p1 < p2:
            hgt = min(height[p1], height[p2])
            wdt = p2 - p1
            max_w = max(max_w, hgt * wdt)

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_w


if __name__ == "__main__":
    height = [random.randint(1, 100) for _ in range(1000)]

    sol1 = Solution1()
    sol2 = Solution2()

    sol1.run(height)
    sol2.run(height)
