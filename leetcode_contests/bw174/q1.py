from collections import defaultdict


class Solution:
    def bestTower(
        self,
        towers: list[list[int]],
        center: list[int],
        radius: int,
    ) -> list[int]:
        def md(
            x: tuple[int, int],
            y: tuple[int, int],
            radius: int,
        ) -> bool:
            return abs(x[0] - y[0]) + abs(x[1] - y[1]) <= radius

        results = defaultdict(list)
        maxi = -1
        for t in towers:
            if md((t[0], t[1]), (center[0], center[1]), radius):
                maxi = max(maxi, t[2])
                results[t[2]].append(t)

        if maxi == -1:
            return [-1, -1]

        res = results[maxi][0]
        for t in results[maxi]:
            if t[0] < res[0]:
                res = t
            elif t[0] == res[0] and t[1] < res[1]:
                res = t
        return [res[0], res[1]]


if __name__ == "__main__":
    print(
        Solution().bestTower(
            towers=[[5, 6, 8], [0, 3, 5]],
            center=[1, 2],
            radius=1,
        )
    )
