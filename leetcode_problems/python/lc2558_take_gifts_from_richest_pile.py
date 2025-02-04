import math
import heapq


class Solution:
    def pickGifts(
        self,
        gifts: list[int],
        k: int,
    ) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        while k > 0:
            num = -heapq.heappop(heap)
            num = int(math.floor(math.sqrt(num)))
            heapq.heappush(heap, -num)
            k -= 1
        return -sum(heap)


if __name__ == "__main__":
    gifts = [25, 64, 9, 4, 100]
    k = 4
    print(Solution().pickGifts(gifts, k))
