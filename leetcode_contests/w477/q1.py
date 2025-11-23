class Solution:
    def digits(self, num: int) -> list[int]:
        digits = []
        while num > 0:
            sub = num % 10
            if sub > 0:
                digits.append(sub)
            num //= 10
        return list(reversed(digits))

    def sumAndMultiply(self, n: int) -> int:
        digits = self.digits(n)
        ds = 0
        num = 0
        for d in digits:
            ds += d
            num = num * 10 + d
        return num * ds


if __name__ == "__main__":
    print(Solution().sumAndMultiply(1000))
