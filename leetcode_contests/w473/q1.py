class Solution:
    def removeZeros(self, n: int) -> int:
        num = []
        while n > 0:
            i = n % 10
            if i != 0:
                num.append(i)
            n = n // 10
        return int("".join(str(x) for x in reversed(num)))


if __name__ == "__main__":
    n = 1020030
    sol = Solution()
    print(sol.removeZeros(n))
