class Solution:
    def carPooling(
        self,
        trips: list[list[int]],
        capacity: int,
    ) -> bool:
        points = []
        for trip in trips:
            points.append([trip[1], trip[0]])
            points.append([trip[2], -trip[0]])

        points.sort()
        curmax = 0
        for point in points:
            curmax += point[1]
            if curmax > capacity:
                return False
        return True


if __name__ == "__main__":
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 5
    print(Solution().carPooling(trips, capacity))
