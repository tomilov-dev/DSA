class Solution:
    def run(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(t) and s[p1] == t[p2]:
            p1 += 1
            p2 += 1

        if len(s) == len(t):
            p1 += 1
            p2 += 1
        elif len(s) > len(t):
            p1 += 1
        else:
            p2 += 1

        return s[p1:] == t[p2:]


class Solution2:
    def run(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            return self.run(t, s)

        if len(s) - len(t) > 1:
            return False

        for i in range(len(t)):
            if s[i] == t[i]:
                continue
            if len(s) == len(t):
                return s[i + 1 :] == t[i + 1 :]
            return s[i + 1 :] == t[i:]

        return len(t) + 1 == len(s)


if __name__ == "__main__":
    s = "aabca"
    t = "aaca"

    s = "aaca"
    t = "aabca"

    s = "aabca"
    t = "aadca"
    print(Solution().run(s, t))
