class Solution:
    def isPalindrome(self, s: str) -> list[list[bool]]:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or is_palindrome[i + 1][j - 1]):
                    is_palindrome[i][j] = True
        return is_palindrome

    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = self.isPalindrome(s)
        dp = [n] * n
        dp[0] = 0
        for i in range(1, n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i, 0, -1):
                    if is_palindrome[j][i]:
                        dp[i] = min(dp[i], 1 + dp[j - 1])
        return dp[n - 1]


if __name__ == "__main__":
    s = "aab"
    print(Solution().minCut(s))
