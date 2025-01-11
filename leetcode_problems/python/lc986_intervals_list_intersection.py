class Solution:
    def is_intersected(
        self,
        i1: list[int],
        i2: list[int],
    ) -> bool:
        return max(i1[0], i2[0]) <= min(i1[1], i2[1])

    def intersection(
        self,
        i1: list[int],
        i2: list[int],
    ) -> list[int]:
        return [max(i1[0], i2[0]), min(i1[1], i2[1])]

    def intervalIntersection(
        self,
        firstList: list[list[int]],
        secondList: list[list[int]],
    ) -> list[list[int]]:
        res = []
        j = 0
        for i1 in firstList:
            for i in range(j, len(secondList)):
                i2 = secondList[i]
                if self.is_intersected(i1, i2):
                    res.append(self.intersection(i1, i2))
                if i1[1] > i2[0]:
                    j = i

        return res


class Solution2:
    def is_intersected(
        self,
        i1: list[int],
        i2: list[int],
    ) -> bool:
        return max(i1[0], i2[0]) <= min(i1[1], i2[1])

    def intersection(
        self,
        i1: list[int],
        i2: list[int],
    ) -> list[int]:
        return [max(i1[0], i2[0]), min(i1[1], i2[1])]

    def intervalIntersection(
        self,
        firstList: list[list[int]],
        secondList: list[list[int]],
    ) -> list[list[int]]:
        res = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            if self.is_intersected(firstList[i], secondList[j]):
                res.append(self.intersection(firstList[i], secondList[j]))

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res


if __name__ == "__main__":
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    out = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    print(Solution().intervalIntersection(firstList, secondList))
