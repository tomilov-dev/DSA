import heapq


class Solution:
    def maxScore(
        self,
        nums1: list[int],
        nums2: list[int],
        k: int,
    ) -> int:
        heap = []
        total = 0
        res = 0
        pairs = list(zip(nums1, nums2))
        pairs.sort(key=lambda x: -x[1])
        for x, y in pairs:
            if len(heap) + 1 > k:
                total -= heapq.heappop(heap)
            heapq.heappush(heap, x)
            total += x
            if len(heap) == k:
                res = max(res, total * y)
        return res
