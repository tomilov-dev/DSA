class Solution:
    def residuePrefixes(self, s: str) -> int:
        total = 0
        seen = set()
        for i in range(len(s)):
            seen.add(s[i])
            if len(seen) == (i + 1) % 3:
                total += 1
        return total


if __name__ == "__main__":
    print(Solution().residuePrefixes("bob"))
