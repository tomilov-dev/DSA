class SolutionRecursion:
    def minDistance(self, word1: str, word2: str) -> int:
        def rec(i: int, j: int) -> int:
            if i == n:
                return m - j
            if j == m:
                return n - i
            if word1[i] == word2[j]:
                return rec(i + 1, j + 1)
            return 1 + min(
                rec(i + 1, j + 1),  # replace
                rec(i, j + 1),  # insert
                rec(i + 1, j),  # delete
            )

        n = len(word1)
        m = len(word2)
        return rec(0, 0)


class SolutionTopDown:
    def minDistance(self, word1: str, word2: str) -> int:
        def rec(i: int, j: int) -> int:
            if i == n:
                return m - j
            if j == m:
                return n - i
            if word1[i] == word2[j]:
                return rec(i + 1, j + 1)
            key = (i, j)
            if key not in mem:
                mem[key] = 1 + min(
                    rec(i + 1, j + 1),  # replace
                    rec(i, j + 1),  # insert
                    rec(i + 1, j),  # delete
                )
            return mem[key]

        n = len(word1)
        m = len(word2)
        mem = {}
        return rec(0, 0)


class SolutionBottomUp:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  # replace
                        dp[i][j - 1],  # insert
                        dp[i - 1][j],  # delete
                    )
        return dp[n][m]


class SolutionBottomUpBackward:
    def minDistance(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n:
                    dp[i][j] = m - j
                elif j == m:
                    dp[i][j] = n - i
                elif word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j + 1],  # replace
                        dp[i][j + 1],  # insert
                        dp[i + 1][j],  # delete
                    )
        return dp[0][0]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    sol = SolutionBottomUp()
    print(sol.minDistance(word1, word2))
