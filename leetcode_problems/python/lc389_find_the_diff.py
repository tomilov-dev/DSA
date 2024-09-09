from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        smap = Counter(s)
        tmap = Counter(t)

        for char in tmap:
            if char not in smap:
                return char
            scount = smap[char]
            if scount < tmap[char]:
                return char


if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t))
