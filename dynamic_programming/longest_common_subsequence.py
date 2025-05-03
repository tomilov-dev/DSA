class Solution:
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
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1],
                    )
        return dp[m][n]


class SolutionOptimized:
    def lcs(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            new_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    new_dp[j] = dp[j - 1] + 1
                else:
                    new_dp[j] = max(
                        dp[j],
                        dp[j - 1],
                    )
            dp = new_dp
        return dp[n]


class SolutionSuperOptimized:
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
            ndp = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    ndp[j] = dp[j - 1] + 1
                else:
                    ndp[j] = max(
                        dp[j],
                        dp[j - 1],
                    )
            dp, ndp = ndp, dp
        return dp[n]


if __name__ == "__main__":
    s1 = "ABCDGH"
    s2 = "AEDFHR"

    s1 = "ABC"
    s2 = "AC"

    s1 = "XYZW"
    s2 = "XYWZ"

    s1 = "XXYZ"
    s2 = "XAYZ"
    print(Solution().lcs(s1, s2))
    print(SolutionOptimized().lcs(s1, s2))
    print(SolutionSuperOptimized().lcs(s1, s2))
