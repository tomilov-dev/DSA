import heapq


class Solution:
    def getFinalState(
        self,
        nums: list[int],
        k: int,
        m: int,
    ) -> list[int]:
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)
        for _ in range(k):
            num, i = heapq.heappop(heap)
            num *= m
            heapq.heappush(heap, (num, i))
            nums[i] = num
        return nums


if __name__ == "__main__":
    nums = [2, 1, 3, 5, 6]
    k = 5
    multiplier = 2
    print(Solution().getFinalState(nums, k, multiplier))
