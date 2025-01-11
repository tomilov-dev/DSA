class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rx = 0
        while x:
            i = x % 10
            rx = rx * 10 + i
            x //= 10

        rx *= sign
        if rx < -(2**31) or rx > 2**31 - 1:
            return 0

        return rx


if __name__ == "__main__":
    n = -123
    print(Solution().reverse(n))
