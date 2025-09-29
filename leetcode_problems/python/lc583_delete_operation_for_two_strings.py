class SolutionRecursive:
    def minDistance(self, word1: str, word2: str) -> int:
        def rec(i: int, j: int) -> int:
            if i >= n and j >= m:
                return 0
            if i >= n:
                return m - j
            if j >= m:
                return n - i

            if word1[i] == word2[j]:
                return rec(i + 1, j + 1)
            else:
                return 1 + min(
                    rec(i + 1, j),
                    rec(i, j + 1),
                )

        n = len(word1)
        m = len(word2)
        return rec(0, 0)


class SolutionTopDown:
    def minDistance(self, word1: str, word2: str) -> int:
        def rec(i: int, j: int) -> int:
            if i >= n and j >= m:
                return 0
            if i >= n:
                return m - j
            if j >= m:
                return n - i

            key = (i, j)
            if key not in mem:
                if word1[i] == word2[j]:
                    mem[key] = rec(i + 1, j + 1)
                else:
                    mem[key] = 1 + min(
                        rec(i + 1, j),
                        rec(i, j + 1),
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
        # базовый случай когда word1 пустая строка
        for j in range(m + 1):
            dp[0][j] = j
        # базовый случай когда word2 пустая строка
        for i in range(n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
        return dp[n][m]


if __name__ == "__main__":
    word1 = "sea"
    word2 = "eat"
    sol = SolutionBottomUp()
    print(sol.minDistance(word1, word2))
