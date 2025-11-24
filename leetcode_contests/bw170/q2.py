class Solution:
    def parseDigits(self, num: int) -> list[int]:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        return list(reversed(digits))

    def picksWalleys(self, digits: list[int]) -> int:
        if len(digits) < 3:
            return 0
        res = 0
        for i in range(1, len(digits) - 1):
            if digits[i - 1] < digits[i] and digits[i + 1] < digits[i]:
                res += 1
                continue
            if digits[i] < digits[i - 1] and digits[i] < digits[i + 1]:
                res += 1
                continue
        return res

    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for x in range(num1, num2 + 1):
            d = self.parseDigits(x)
            res += self.picksWalleys(d)
        return res


if __name__ == "__main__":
    # print(Solution().totalWaviness(198, 202))
    print(Solution().totalWaviness(4848, 4848))
