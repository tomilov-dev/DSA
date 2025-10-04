class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(n):
            xor ^= start + 2 * i
        return xor


if __name__ == "__main__":
    n = 5
    start = 0
    print(Solution().xorOperation(n, start))
