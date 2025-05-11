class Solution:
    def editDistance(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],  # deletion = delete (1) + previous
                        dp[i][j - 1],  # insertion = insert in s1 (1) + previous
                        dp[i - 1][j - 1],  # replacement = replace (1) + previous
                    )

        return dp[m][n]


class SolutionOptimized:
    def editDistance(
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
                if s1[i - 1] == s2[j - 1]:
                    ndp[j] = dp[j - 1]
                else:
                    ndp[j] = 1 + min(
                        ndp[j],  # deletion
                        dp[i - 1],  # insertion
                        dp[j - 1],  # replacement
                    )
            dp, ndp = ndp, dp

        return dp[n]


if __name__ == "__main__":
    s1 = "geek"
    s2 = "gesek"
    print(Solution().editDistance(s1, s2))
    print(SolutionOptimized().editDistance(s1, s2))
