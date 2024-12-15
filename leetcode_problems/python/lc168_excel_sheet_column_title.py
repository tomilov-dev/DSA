class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = [chr(64 + i) for i in range(1, 27)]
        stack = []
        num = columnNumber
        while num > 0:
            num -= 1
            stack.append(chars[num % 26])
            num //= 26

        return "".join(reversed(stack))


if __name__ == "__main__":
    columnNumber = 701
    print(Solution().convertToTitle(columnNumber))
