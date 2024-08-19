class Solution:
    def splitNum(self, num: int) -> int:
        digits = []

        rem = num
        while rem > 0:
            digits.append(rem % 10)
            rem //= 10

        digits.sort()

        num1 = 0
        num2 = 0
        for index, digit in enumerate(digits):
            if index % 2 == 0:
                num1 = num1 * 10 + digit
            else:
                num2 = num2 * 10 + digit

        return num1 + num2


if __name__ == "__main__":
    num = 4325
    print(Solution().splitNum(num))
