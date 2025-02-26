class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        dp = [[False] * len(s) for _ in range(len(s))]
        start = 0
        max_length = 1
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        return s[start : start + max_length]


if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))
