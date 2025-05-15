class Solution:
    def lcs(self, s1: str, s2: str) -> int:
        def rec(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0
            if s1[i - 1] == s2[j - 1]:
                return 1 + rec(i - 1, j - 1)
            return max(rec(i, j - 1), rec(i - 1, j))

        return rec(len(s1), len(s2))


if __name__ == "__main__":
    s1 = "abc"
    s2 = "adc"
    print(Solution().lcs(s1, s2))
