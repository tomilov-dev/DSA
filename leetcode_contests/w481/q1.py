class Solution:
    def mirrorDistance(self, n: int) -> int:
        def rev(n: int) -> int:
            digits = []
            while n > 0:
                digits.append(n % 10)
                n //= 10
            num = 0
            for d in digits:
                num = 10 * num + d
            return num

        return abs(n - rev(n))


if __name__ == "__main__":
    n = 25
    n = 10
    n = 7
    print(Solution().mirrorDistance(n))
