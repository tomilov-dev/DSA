class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1


if __name__ == "__main__":
    print(Solution2().isPowerOfTwo(9))
