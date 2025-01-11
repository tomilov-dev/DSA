class Solution:
    def eraseOverlapIntervals(
        self,
        intervals: list[list[int]],
    ) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]

        return count


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

    intervals = [
        [-52, 31],
        [-73, -26],
        [82, 97],
        [-65, -11],
        [-62, -49],
        [95, 99],
        [58, 95],
        [-31, 49],
        [66, 98],
        [-63, 2],
        [30, 47],
        [-40, -26],
    ]

    print(Solution().eraseOverlapIntervals(intervals))
