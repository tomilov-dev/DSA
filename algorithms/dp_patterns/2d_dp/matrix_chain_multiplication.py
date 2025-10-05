MAX = 10**9


class Solution:
    def matrix_chain_order(self, p: list[int]) -> int:
        n = len(p) - 1
        dp = [[0] * n for _ in range(n)]

        for l in range(2, n + 1):  # Длина подцепочки от 2 до n
            for i in range(n - l + 1):  # Начальная матрица
                j = i + l - 1  # Конечная матрица
                dp[i][j] = MAX
                for k in range(i, j):  # Точка разбиения
                    cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1]
