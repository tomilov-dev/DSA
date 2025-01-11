class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = dict()
        for c in s:
            m[c] = m.get(c, 0) + 1

        for c in t:
            if c not in m or m[c] <= 0:
                return False
            if m[c] == 1:
                del m[c]
                continue
            m[c] -= 1

        return not m


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
