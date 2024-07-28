class Solution:
    def help(self, s: str, p1: int, p2: int) -> bool:
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            char1 = s[p1]
            char2 = s[p2]

            if char1 == char2:
                p1 += 1
                p2 -= 1

            else:
                return self.help(s, p1 + 1, p2) or self.help(s, p1, p2 - 1)

        return True


if __name__ == "__main__":
    s = "abca"
    s = "abc"
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

    print(Solution().validPalindrome(s))
