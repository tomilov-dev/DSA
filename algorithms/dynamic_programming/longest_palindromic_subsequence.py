class SolutionRecursive:
    def longestPalinSubseq(self, s: str) -> int:
        def rec(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1

            if s[i] == s[j]:
                return 2 + rec(i + 1, j - 1)
            return max(rec(i + 1, j), rec(i, j - 1))

        return rec(0, len(s) - 1)


class SolutionTopDown:
    def longestPalinSubseq(self, s: str) -> int:
        def rec(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1

            key = (i, j)
            if key not in mem:
                if s[i] == s[j]:
                    mem[key] = 2 + rec(i + 1, j - 1)
                else:
                    mem[key] = max(rec(i + 1, j), rec(i, j - 1))
            return mem[key]

        mem = {}
        return rec(0, len(s) - 1)


class SolutionBottomUp:
    def longestPalinSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue

                if s[i] == s[j]:
                    if i + 1 == j:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


class SolutionBottomUpOptimized:
    def longestPalinSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ndp = [0] * n

        for i in range(n - 1, -1, -1):
            ndp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    ndp[j] = 2 + dp[j - 1]
                else:
                    ndp[j] = max(dp[j], ndp[j - 1])
            dp, ndp = ndp, dp

        return ndp[n - 1]


if __name__ == "__main__":
    s = "bbabcbcab"
    print(SolutionRecursive().longestPalinSubseq(s))
    print(SolutionTopDown().longestPalinSubseq(s))
    print(SolutionBottomUp().longestPalinSubseq(s))
    print(SolutionBottomUpOptimized().longestPalinSubseq(s))
