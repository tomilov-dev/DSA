import bisect


class ExamTracker:
    def __init__(self) -> None:
        self._times = []
        self._scores = []
        self._pref = []

    def record(self, time: int, score: int) -> None:
        self._times.append(time)
        self._scores.append(score)
        prev = 0
        if len(self._pref) > 0:
            prev = self._pref[-1]
        self._pref.append(prev + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        start = bisect.bisect_left(self._times, startTime)
        end = bisect.bisect_right(self._times, endTime) - 1
        if start >= len(self._times) or end < 0 or start > end:
            return 0
        return self._pref[end] - (self._pref[start - 1] if start > 0 else 0)


if __name__ == "__main__":
    tracker = ExamTracker()
    tracker.record(1, 98)
    print(tracker.totalScore(1, 1))
    tracker.record(5, 99)
    print(tracker.totalScore(1, 3))
    print(tracker.totalScore(1, 5))
    print(tracker.totalScore(3, 4))
    print(tracker.totalScore(2, 5))
    # tracker.record()
