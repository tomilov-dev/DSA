class Solution:
    def numberOfLines(
        self,
        widths: list[int],
        s: str,
    ) -> list[int]:
        lines_count = 1
        line = 0

        for index in range(len(s)):
            char = s[index]
            width = widths[ord(char) - ord("a")]

            if line + width > 100:
                lines_count += 1
                line = width

            else:
                line += width

        return [lines_count, line]


if __name__ == "__main__":
    widths = [
        4,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
    ]
    s = "bbbcccdddaaa"

    print(Solution().numberOfLines(widths, s))
