class Solution:
    def busyStudent(
        self,
        startTime: list[int],
        endTime: list[int],
        queryTime: int,
    ) -> int:
        return sum(
            startTime[i] <= queryTime <= endTime[i] for i in range(len(startTime))
        )


if __name__ == "__main__":
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4
    print(Solution().busyStudent(startTime, endTime, queryTime))
