import heapq


class Solution:
    def findRelativeRanks(
        self,
        score: list[int],
    ) -> list[str]:
        mapping = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal",
        }

        res = [(score[i], i) for i in range(len(score))]
        res.sort(reverse=True)
        for i, sc in enumerate(res):
            v, j = sc
            score[j] = mapping.get(i, str(i + 1))
        return score


class SolutionHeap:
    def findRelativeRanks(
        self,
        score: list[int],
    ):
        mapping = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal",
        }

        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)

        rank = 0
        while heap:
            _, i = heapq.heappop(heap)
            score[i] = mapping.get(rank, str(rank + 1))
            rank += 1

        return score


if __name__ == "__main__":
    score = [5, 4, 3, 2, 1]
    print(SolutionHeap().findRelativeRanks(score))
