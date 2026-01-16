import heapq
from collections import defaultdict


class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        n = len(nums1)
        sm = 0
        prev = 0

        heap = []
        res = [0] * n

        index = sorted(range(n), key=lambda x: nums1[x])
        for i in index:
            num1, num2 = nums1[i], nums2[i]

            if prev < num1:
                prev_sum = sm
            res[i] = prev_sum

            prev = num1
            sm += num2
            if len(heap) == k:
                sm -= heapq.heappushpop(heap, num2)
            else:
                heapq.heappush(heap, num2)

        return res


if __name__ == "__main__":
    nums1 = [4, 2, 1, 5, 3]
    nums2 = [10, 20, 30, 40, 50]
    k = 2
    print(Solution().findMaxSum(nums1, nums2, k))
