class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_s = (s + s)[1:-1]
        return s in doubled_s


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abab"))
    print(Solution().repeatedSubstringPattern("aba"))
    print(Solution().repeatedSubstringPattern("abcabcabcabc"))
