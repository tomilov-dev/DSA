class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for char in columnTitle:
            num = num * 26 + (ord(char) - ord("A") + 1)
        return num


if __name__ == "__main__":
    columnTitle = "AB"
    print(Solution().titleToNumber(columnTitle))
