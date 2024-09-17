class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) <= 1:
            return s

        ls = list(s)

        p1 = 0
        p2 = 0
        sp = 0
        while sp < len(s):
            while sp < len(s) and ls[sp] != " ":
                sp += 1

            p2 = sp - 1
            while p1 < p2:
                ls[p1], ls[p2] = ls[p2], ls[p1]
                p1 += 1
                p2 -= 1

            sp += 1
            p1 = sp

        return "".join(ls)


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))
