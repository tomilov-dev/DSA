class Solution:
    def largestEven(self, s: str) -> str:
        i = len(s) - 1
        while i >= 0 and s[i] == "1":
            i -= 1
        if i == -1:
            return ""
        return s[: i + 1]
