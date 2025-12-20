class SolutionDPWrong:
    def maximumScore(self, nums: list[int], s: str) -> int:
        def rec(i: int, prev: bool):
            if i < 0:
                return 0

            key = (i, prev)
            if key in mem:
                return mem[key]

            if not prev and s[i] == "1":
                score = max(
                    nums[i] + rec(i - 1, False),
                    rec(i - 1, True),
                )
            elif not prev and s[i] == "0":
                score = rec(i - 1, False)
            elif prev and s[i] == "1":
                score = max(
                    nums[i] + rec(i - 1, False),
                    rec(i - 1, True),
                )
            elif prev and s[i] == "0":
                score = max(
                    nums[i] + rec(i - 1, False),
                    rec(i - 1, True),
                )

            mem[key] = score
            return score

        mem = dict()
        n = len(nums)
        return rec(n - 1, False)


import heapq


class Solution:
    def maximumScore(self, nums: list[int], s: str) -> int:
        n = len(nums)
        heap = []
        total = 0
        for i in range(n):
            heapq.heappush(heap, -nums[i])
            if s[i] == "1":
                total += -heapq.heappop(heap)
        return total


if __name__ == "__main__":
    nums = [2, 1, 5, 2, 3]
    s = "01010"

    nums = [4, 7, 2, 9]
    s = "0000"

    nums = [8, 1, 7, 1, 3, 7, 5, 6, 10, 10]
    s = "0010111000"
    print(Solution().maximumScore(nums, s))
