class Solution:
    def maxPower(self, s: str) -> int:
        c = 0
        index = 0
        while index < len(s):
            cc = 1
            char = s[index]
            while index + 1 < len(s) and char == s[index + 1]:
                cc += 1
                index += 1

            c = max(c, cc)
            index += 1

        return c


if __name__ == "__main__":
    s = "abbcccddddeeeeedcba"
    print(Solution().maxPower(s))
