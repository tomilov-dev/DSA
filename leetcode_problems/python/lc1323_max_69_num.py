class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = []
        rem = num
        while rem > 0:
            digits.append(rem % 10)
            rem //= 10

        digits.reverse()

        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break

        num = 0
        grade = len(digits) - 1
        for digit in digits:
            num += digit * 10**grade
            grade -= 1

        return num


if __name__ == "__main__":
    # num = 9996
    num = 9669
    print(Solution().maximum69Number(num))
