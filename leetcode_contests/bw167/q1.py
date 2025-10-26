class Solution:
    def scoreBalance(self, s: str) -> bool:
        full = 0
        for char in s:
            sc = ord(char) - ord("a") + 1
            full += sc

        part = 0
        for char in s:
            sc = ord(char) - ord("a") + 1
            part += sc
            full -= sc
            if part == full:
                return True
        return False


if __name__ == "__main__":
    print(Solution().scoreBalance("bace"))
