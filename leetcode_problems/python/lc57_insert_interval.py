class Solution:
    def is_intersected(
        self,
        i1: list[int],
        i2: list[int],
    ) -> bool:
        return max(i1[0], i2[0]) <= min(i1[1], i2[1])

    def combine(
        self,
        i1: list[int],
        i2: list[int],
    ) -> list[int]:
        return [min(i1[0], i2[0]), max(i1[1], i2[1])]

    def insert(
        self,
        intervals: list[list[int]],
        newInterval: list[int],
    ) -> list[list[int]]:
        res = []
        index = None
        for interval in intervals:
            intersected = self.is_intersected(interval, newInterval)
            if not intersected:
                res.append(interval)
                continue

            if index is None:
                combined = self.combine(interval, newInterval)
                index = len(res)
                res.append(combined)
            else:
                res[index] = self.combine(interval, res[index])

        if index is None:
            res.append(newInterval)
            res.sort()
            return res
        else:
            return res


if __name__ == "__main__":
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(Solution().insert(intervals, newInterval))
