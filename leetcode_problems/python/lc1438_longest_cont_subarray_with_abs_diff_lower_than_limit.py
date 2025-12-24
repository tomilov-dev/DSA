import heapq


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxq = []
        minq = []

        i = 0
        maxi = 0
        for j, num in enumerate(nums):
            heapq.heappush(maxq, [-num, j])
            heapq.heappush(minq, [num, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            maxi = max(maxi, j - i + 1)
        return maxi


if __name__ == "__main__":
    print(Solution().longestSubarray([8, 2, 4, 7], 4))
