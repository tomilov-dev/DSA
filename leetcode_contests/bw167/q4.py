class Solution:
    def maxPartitionFactor(self, points: list[list[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def calc_min_dist(group: list[list[int]]) -> int:
            if len(group) < 2:
                return float("inf")
            mini = float("inf")
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    mini = min(mini, manhattan(group[i], group[j]))
            return mini

        def backtrack(i: int):
            nonlocal maxi

            if i == n:
                if len(group1) > 0 and len(group2) > 0:
                    min1 = calc_min_dist(group1)
                    min2 = calc_min_dist(group2)
                    maxi = max(maxi, min(min1, min2))
                return

            group1.append(points[i])
            backtrack(i + 1)
            group1.pop()

            group2.append(points[i])
            backtrack(i + 1)
            group2.pop()

        n = len(points)
        if n == 2:
            return 0

        group1 = []
        group2 = []
        maxi = 0
        backtrack(0)
        return maxi


if __name__ == "__main__":
    points = [[0, 0], [0, 2], [2, 0], [2, 2]]
    print(Solution().maxPartitionFactor(points))
