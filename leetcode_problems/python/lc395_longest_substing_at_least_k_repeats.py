"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
if no such substring exists, return 0.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) < k:
            return 0
        if k <= 1:
            return len(s)

        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for char in freq:
            if freq[char] < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))

        return len(s)


if __name__ == "__main__":
    s = "ababbc"
    k = 2

    s = "aaabbb"
    k = 3

    s = "bbaaacbd"
    k = 3

    print(Solution().longestSubstring(s, k))
