class Solution:
    def countBits(self, n: int) -> list[int]:
        return [i.bit_count() for i in range(0, n + 1)]


if __name__ == "__main__":
    print(Solution().countBits(2))
