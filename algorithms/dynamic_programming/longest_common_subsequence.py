class SolutionRecursive:
    def lcs(
        self,
        s1: str,
        s2: str,
    ) -> int:
        def rec(i: int, j: int, c: int = 0) -> int:
            if i >= len(s1) or j >= len(s2):
                return c

            return max(
                rec(i + 1, j + 1, c + int(s1[i] == s2[j])),
                rec(i + 1, j, c),
                rec(i, j + 1, c),
            )

        return rec(0, 0)


class SolutionTopDown:
    def lcs(
        self,
        s1: str,
        s2: str,
    ) -> int:
        def rec(i: int, j: int, c: int = 0) -> int:
            if i >= len(s1) or j >= len(s2):
                return c

            key = (i, j, c)
            if key not in mem:
                mem[key] = max(
                    rec(i + 1, j + 1, c + int(s1[i] == s2[j])),
                    rec(i + 1, j, c),
                    rec(i, j + 1, c),
                )
            return mem[key]

        mem = {}
        return rec(0, 0)


class SolutionBottomUp:
    def lcs(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1] + int(s1[i - 1] == s2[j - 1]),
                )
        return dp[m][n]


class SolutionBottomUpOptimized:
    def lcs(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ndp[j] = max(
                    dp[j],
                    ndp[j - 1],
                    dp[j - 1] + int(s1[i - 1] == s2[j - 1]),
                )
            dp, ndp = ndp, dp
        return dp[n]


if __name__ == "__main__":
    s1 = "ABCDGH"
    s2 = "AEDFHR"

    s1 = "ABC"
    s2 = "AC"

    # s1 = "XYZW"
    # s2 = "XYWZ"

    s1 = "XXYZ"
    s2 = "XAYZ"

    print(SolutionRecursive().lcs(s1, s2))
    print(SolutionTopDown().lcs(s1, s2))
    print(SolutionBottomUp().lcs(s1, s2))
    print(SolutionBottomUpOptimized().lcs(s1, s2))
