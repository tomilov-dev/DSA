class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        p1 = 0
        p2 = 0

        maxi = 0
        used = set([s[p2]])
        while p1 < len(s):
            while p2 + 1 < len(s) and s[p2 + 1] not in used:
                p2 += 1
                used.add(s[p2])

            maxi = max(maxi, p2 - p1 + 1)
            used.remove(s[p1])
            p1 += 1

            if p1 < p2 < len(s):
                p2 = p1
                used = set([s[p2]])

        return maxi


if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
