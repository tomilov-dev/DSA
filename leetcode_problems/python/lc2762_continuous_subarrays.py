from collections import deque


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        i = 0
        total = 0
        minq = deque()
        maxq = deque()
        for j, num in enumerate(nums):
            while minq and nums[minq[-1]] >= num:
                minq.pop()
            while maxq and nums[maxq[-1]] <= num:
                maxq.pop()

            minq.append(j)
            maxq.append(j)

            while nums[maxq[0]] - nums[minq[0]] > 2:
                i += 1
                if minq[0] < i:
                    minq.popleft()
                if maxq[0] < i:
                    maxq.popleft()

            total += j - i + 1

        return total


if __name__ == "__main__":
    nums = [5, 4, 2, 4]
    print(Solution().continuousSubarrays(nums))
