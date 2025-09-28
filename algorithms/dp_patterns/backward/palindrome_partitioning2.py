MAX = 10**7


class SolutionRecursion:
    def minCut(self, s: str) -> int:
        def is_palindrome(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def rec(i: int, j: int) -> int:
            if i >= j and j - i == 1:
                return 0
            if is_palindrome(i, j):
                return 0

            mini = MAX
            for k in range(i, j):
                mini = min(
                    mini,
                    1 + rec(i, k) + rec(k + 1, j),
                )
            return mini

        n = len(s)
        return rec(0, n - 1)


class SolutionTopDown:
    def minCut(self, s: str) -> int:
        def is_palindrome(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def rec(i: int, j: int) -> int:
            if i >= j and j - i == 1:
                return 0
            if is_palindrome(i, j):
                return 0

            key = (i, j)
            if key not in mem:
                mini = MAX
                for k in range(i, j):
                    mini = min(
                        mini,
                        1 + rec(i, k) + rec(k + 1, j),
                    )
                mem[key] = mini
            return mem[key]

        n = len(s)
        mem = {}
        return rec(0, n - 1)


class SolutionBottomUp:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            palindrome[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        dp = [MAX] * n
        for j in range(n):
            if palindrome[0][j]:
                dp[j] = 0
            else:
                for i in range(1, j + 1):
                    if palindrome[i][j]:
                        dp[j] = min(dp[j], 1 + dp[i - 1])
        return dp[n - 1]


class SolutionBottomUpBackward:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            palindrome[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        dp = [MAX] * (n + 1)
        dp[n] = -1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if palindrome[i][j]:
                    dp[i] = min(dp[i], 1 + dp[j + 1])
        return dp[0]


if __name__ == "__main__":
    s = "aab"  # 1 cut, "aab" -> "aa" | "b"
    # s = "racecar"  # 0 cuts, already palindrome
    # s = "abc"  # 2 cuts, "abc" -> "a" | "b" | "c"
    # s = "aabbc"  # 3 cuts, "aabbc" -> "aa" | "bb" | "c"

    sol = SolutionBottomUpBackward()
    print(sol.minCut(s))
