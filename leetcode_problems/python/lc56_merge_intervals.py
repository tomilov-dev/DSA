class Solution:
    def is_intersect(
        self,
        i1: list[int],
        i2: list[int],
    ) -> bool:
        return max(i1[0], i2[0]) <= min(i1[1], i2[1])

    def merged(
        self,
        i1: list[int],
        i2: list[int],
    ) -> list[int]:
        return [min(i1[0], i2[0]), max(i1[1], i2[1])]

    def merge(
        self,
        intervals: list[list[int]],
    ) -> list[list[int]]:
        if len(intervals) == 0:
            return intervals

        intervals.sort(key=lambda x: x[0])
        overlap = [intervals[0]]
        for interval in intervals[1:]:
            prev = overlap[-1]
            if self.is_intersect(prev, interval):
                overlap[-1] = self.merged(prev, interval)
            else:
                overlap.append(interval)

        return overlap


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))
