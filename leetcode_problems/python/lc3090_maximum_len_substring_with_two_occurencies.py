class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if not s:
            return 0

        mem = {s[0]: 1}
        p1 = 0
        p2 = 0
        maxi = 1
        while p1 < len(s) and p2 < len(s):
            while p2 + 1 < len(s) and mem.get(s[p2 + 1], 0) < 2:
                p2 += 1
                mem[s[p2]] = mem.get(s[p2], 0) + 1

            maxi = max(maxi, p2 - p1 + 1)
            mem[s[p1]] = max(0, mem.get(s[p1], 0) - 1)
            p1 += 1

        return maxi


if __name__ == "__main__":
    s = "bcbbbcba"
    s = "aaaa"
    print(Solution().maximumLengthSubstring(s))
