"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
"""

import math
import random


class Solution:
    def transform(self, x: int, y: int) -> tuple[int, int, float]:
        return x, y, math.sqrt(((0 - x) ** 2) + ((0 - y) ** 2))

    def quick_select(
        self,
        points: list[tuple[int, int, float]],
        k: int,
    ):
        if not points:
            return

        x = random.choice(points)
        xv = x[2]

        left = [p for p in points if p[2] < xv]
        mid = [p for p in points if p[2] == xv]
        right = [p for p in points if p[2] > xv]

        if k < len(left):
            return self.quick_select(left, k)
        elif k > len(left) + len(mid):
            return left + mid + self.quick_select(right, k - len(left) - len(mid))
        else:
            return left + mid[: k - len(left)]

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        transformed_points = [self.transform(x, y) for x, y in points]
        closest_points = self.quick_select(transformed_points, k)
        return [[x, y] for x, y, _ in closest_points]


if __name__ == "__main__":
    points = [[1, 3], [-2, 2]]
    k = 1

    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2

    sol = Solution()
    res = sol.kClosest(points, k)

    print(res)
