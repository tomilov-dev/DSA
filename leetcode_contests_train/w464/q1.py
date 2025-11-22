import math


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = 0
        even = 0
        for x in range(2 * n + 1):
            if x % 2 == 0:
                even += x
            else:
                odd += x
        return math.gcd(odd, even)
