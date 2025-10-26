class Solution:
    def lexSmallest(self, s: str) -> str:
        def rev(s: str) -> str:
            return "".join(reversed(s))

        sm: str | None = None
        for k in range(len(s)):
            v1 = rev(s[:k]) + s[k:]
            if sm is None:
                sm = v1
            if v1 < sm:
                sm = v1
            v2 = s[:k] + rev(s[k:])
            if v2 < sm:
                sm = v2
        return sm


if __name__ == "__main__":
    s = "dcab"
    # s = "abba"
    # s = "zxy"
    sol = Solution()
    print(sol.lexSmallest(s))
