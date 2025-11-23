class Solution:
    def minimumFlips(self, n: int) -> int:
        origin = list(bin(n)[2:])
        reverse = list(reversed(origin))
        flips = 0
        for i in range(len(origin)):
            if origin[i] != reverse[i]:
                flips += 1
        return flips


if __name__ == "__main__":
    print(Solution().minimumFlips(12))
