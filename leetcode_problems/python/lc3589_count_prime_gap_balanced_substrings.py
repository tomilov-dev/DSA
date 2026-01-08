import math
from collections import deque


class Solution:
    def primeSubarray(self, nums: list[int], k: int) -> int:
        def isPrime(x: int) -> bool:
            if x <= 1:
                return False
            if x in primeMap:
                return primeMap[x]
            for i in range(2, int(math.sqrt(x) + 1)):
                if x % i == 0:
                    primeMap[x] = False
                    return False
            primeMap[x] = True
            return True

        primeMap = dict()
        maxq = deque([])
        minq = deque([])
        primes = deque([])

        l = 0
        total = 0
        for r, x in enumerate(nums):
            if isPrime(x):
                while maxq and x > nums[maxq[-1]]:
                    maxq.pop()
                while minq and x < nums[minq[-1]]:
                    minq.pop()

                primes.append(r)
                maxq.append(r)
                minq.append(r)

                while (
                    len(primes) >= 2
                    and maxq
                    and minq
                    and nums[maxq[0]] - nums[minq[0]] > k
                ):
                    if isPrime(nums[l]):
                        primes.popleft()
                        if maxq[0] == l:
                            maxq.popleft()
                        if minq[0] == l:
                            minq.popleft()
                    l += 1

            if len(primes) >= 2 and nums[maxq[0]] - nums[minq[0]] <= k:
                total += primes[-2] - l + 1

        return total
