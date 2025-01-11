class Solution:
    def run(self, points: list[list[int]]) -> bool:
        mini = min(x for x, y in points)
        maxi = max(x for x, y in points)

        mapper = dict()
        for point in points:
            mapper[tuple(point)] = True

        for x, y in points:
            cx = maxi + mini - x
            if (cx, y) not in mapper:
                return False
        return True


if __name__ == "__main__":
    points = [[1, 1], [-1, 1]]
    print(Solution().run(points))

    points = [[1, 1], [-1, -1]]
    print(Solution().run(points))

    points = [[1, 1], [-1, 1], [2, 2], [-2, 2]]
    print(Solution().run(points))

    points = [[1, 1], [2, 2], [3, 3], [-1, 1], [-2, 2], [-3, 3]]
    print(Solution().run(points))
