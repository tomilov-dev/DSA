class Solution:
    def removeCoveredIntervals(
        self,
        intervals: list[list[int]],
    ) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        prev_end = 0

        for start, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end

        return count


if __name__ == "__main__":
    intervals = [[1, 4], [3, 6], [2, 8]]
    print(Solution().removeCoveredIntervals(intervals))
