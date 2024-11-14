class Solution:
    def is_overlapping(self, a: list[int], b: list[int]) -> bool:
        return max(a[0], b[0]) <= min(a[1], b[1])

    def overlap(self, a: list[int], b: list[int]) -> list[int]:
        return [max(a[0], b[0]), min(a[1], b[1])]

    def findMinArrowShots(
        self,
        points: list[list[int]],
    ) -> int:
        points.sort()
        result = 1
        last = points[0]
        for point in points:
            if self.is_overlapping(last, point):
                last = self.overlap(last, point)
                continue

            last = point
            result += 1

        return result


if __name__ == "__main__":
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(Solution().findMinArrowShots(points))
