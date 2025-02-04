class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        p1 = 0
        p2 = k - 1
        c = 0
        while p1 < len(s) and p2 < len(s):
            sub = s[p1 : p2 + 1]
            if int(sub) > 0:
                c += int(num % int(sub) == 0)
            p1 += 1
            p2 += 1
        return c
