class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        residue = 0

        map = dict()
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

        for cc in map.values():
            if cc % 2 == 0:
                count += cc
            else:
                if cc >= 3:
                    count += cc - 1
                residue += 1

        return count + min(residue, 1)


if __name__ == "__main__":
    s = "abccccdd"
    print(Solution().longestPalindrome(s))
