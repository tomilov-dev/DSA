from collections import deque


class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        maxq = deque()
        minq = deque()
        dp = [0] * (n + 1)
        dp[0] = 1

        acc = 1
        i = 0
        for j, x in enumerate(nums):
            while maxq and nums[maxq[-1]] < x:
                maxq.pop()
            while minq and nums[minq[-1]] > x:
                minq.pop()
            maxq.append(j)
            minq.append(j)

            while nums[maxq[0]] - nums[minq[0]] > k:
                acc = (acc - dp[i]) % MOD
                i += 1
                if minq[0] < i:
                    minq.popleft()
                if maxq[0] < i:
                    maxq.popleft()

            dp[j + 1] = acc
            acc = (acc + dp[j + 1]) % MOD

        return dp[n]


if __name__ == "__main__":
    nums = [9, 4, 1, 3, 7]
    k = 4
    print(Solution().countPartitions(nums, k))
