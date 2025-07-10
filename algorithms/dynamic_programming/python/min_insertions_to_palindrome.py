class SolutionRecursive:
    def findMinInsertions(self, s: str) -> int:
        def rec(i: int, j: int) -> int:
            if i >= j:
                return 0
            if s[i] == s[j]:
                return rec(i + 1, j - 1)
            return 1 + min(
                rec(i + 1, j),
                rec(i, j - 1),
            )

        n = len(s)
        return rec(0, n - 1)


class SolutionTopDown:
    def findMinInsertions(self, s: str) -> int:
        def rec(i: int, j: int) -> int:
            if i >= j:
                return 0

            key = (i, j)
            if key not in mem:
                if s[i] == s[j]:
                    mem[key] = rec(i + 1, j - 1)
                else:
                    mem[key] = 1 + min(
                        rec(i + 1, j),
                        rec(i, j - 1),
                    )
            return mem[key]

        n = len(s)
        mem = dict()
        return rec(0, n - 1)


class SolutionBottomUpLPS:
    def findMinInsertions(self, s: str) -> int:
        n = len(s)
        # dp[i][j] — длина LPS в s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # N - LPS = количество символов, которые надо вставить
        return n - dp[0][n - 1]


class SolutionBottomUp:
    def findMinInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1]
                else:
                    dp[l][r] = 1 + min(
                        dp[l + 1][r],
                        dp[l][r - 1],
                    )
        return dp[0][n - 1]


class SolutionBottomUpOptimized:
    def findMinInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for l in range(n - 2, -1, -1):
            prev = 0
            for h in range(l + 1, n):
                temp = dp[h]
                if s[l] == s[h]:
                    dp[h] = prev
                else:
                    dp[h] = 1 + min(dp[h], dp[h - 1])
            prev = temp
        return dp[n - 1]


if __name__ == "__main__":
    s = "abcd"
    # s = "aba"
    # s = "geeks"
    print(SolutionRecursive().findMinInsertions(s))
    print(SolutionTopDown().findMinInsertions(s))
    print(SolutionBottomUpLPS().findMinInsertions(s))
    print(SolutionBottomUp().findMinInsertions(s))
    print(SolutionBottomUpOptimized().findMinInsertions(s))
