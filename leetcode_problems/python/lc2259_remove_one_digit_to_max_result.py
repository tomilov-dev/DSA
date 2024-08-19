class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = ""
        for index in range(len(number)):
            if number[index] == digit:
                new_number = number[:index] + number[index + 1 :]
                if new_number > max_number:
                    max_number = new_number

        return max_number


if __name__ == "__main__":
    number = "1231"
    digit = "1"

    print(Solution().removeDigit(number, digit))
