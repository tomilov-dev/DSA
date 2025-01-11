import heapq
import random


class Solution:
    def quick_select(
        self,
        values: list[tuple[int, int]],
        k: int,
    ) -> list[tuple[int, int]]:
        if not values:
            return

        x = random.choice(values)
        xv = x[1]

        left = [v for v in values if v[1] > xv]
        mid = [v for v in values if v[1] == xv]
        right = [v for v in values if v[1] < xv]

        if k < len(left):
            return self.quick_select(left, k)
        elif k > len(left) + len(mid):
            return left + mid + self.quick_select(right, k - len(left) - len(mid))
        else:
            return left + mid[: k - len(left)]

    def topKFrequent(
        self,
        nums: list[int],
        k: int,
    ) -> list[int]:
        mem = dict()
        for num in nums:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1

        numz = [(k, v) for k, v in mem.items()]
        result = self.quick_select(numz, k)
        if result:
            return [v[0] for v in result]


class SoltuionWithHeapq:
    def topKFrequent(
        self,
        nums: list[int],
        k: int,
    ) -> list[int]:
        mapper = dict()
        for num in nums:
            mapper[num] = mapper.get(num, 0) + 1

        heap = [(-v, k) for k, v in mapper.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            node = heapq.heappop(heap)
            res.append(node[1])

        return res


class SolutionWithCountingSort:
    def topKFrequent(
        self,
        nums: list[int],
        k: int,
    ) -> list[int]:
        mapper = dict()
        maxn = 0
        for num in nums:
            mapper[num] = mapper.get(num, 0) + 1
            maxn = max(maxn, mapper[num])

        count = [None for _ in range(maxn + 1)]
        for num, fq in mapper.items():
            print(fq)
            if not count[fq]:
                count[fq] = [num]
            else:
                count[fq].append(num)

        res = []
        index = len(count) - 1
        while index > 0 and k > 0:
            if count[index]:
                subindex = 0
                while subindex < len(count[index]) and k > 0:
                    res.append(count[index][subindex])
                    subindex += 1
                    k -= 1
            index -= 1

        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    res = SolutionWithCountingSort().topKFrequent(nums, k)
    print(res)
