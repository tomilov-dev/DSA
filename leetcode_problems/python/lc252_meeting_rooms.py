class Solution:
    def run(self, array: list[list[int]]) -> int:
        points = []
        for interval in array:
            points.append([interval[0], +1])
            points.append([interval[1], -1])

        points.sort()
        maxc = 0
        curc = 0
        for point in points:
            curc += point[1]
            maxc = max(maxc, curc)
        return maxc


if __name__ == "__main__":
    meetings = [[1, 2], [1, 3], [4, 5], [2, 6]]
    print(Solution().run(meetings))
