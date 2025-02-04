class Solution:
    def is_palindrome(
        self,
        string: str,
    ) -> bool:
        p1 = 0
        p2 = len(string) - 1
        while p1 < p2:
            if string[p1] != string[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

    def partition(
        self,
        s: str,
    ) -> list[list[str]]:
        def backtrack(i: int):
            if i >= len(s):
                res.append(stack[:])
                return None

            for j in range(i, len(s)):
                if self.is_palindrome(s[i : j + 1]):
                    stack.append(s[i : j + 1])
                    backtrack(j + 1)
                    stack.pop()

        res = []
        stack = []
        backtrack(0)
        return res


class SolutionDPBacktrack:
    def partition(self, s: str) -> list[list[str]]:
        def backtrack(start: int):
            if start >= len(s):
                res.append(stack[:])
                return

            for end in range(start, len(s)):
                if dp[start][end]:
                    stack.append(s[start : end + 1])
                    backtrack(end + 1)
                    stack.pop()

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        res = []
        stack = []
        backtrack(0)
        return res


if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))
