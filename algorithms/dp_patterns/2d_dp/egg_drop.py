MAX = 10**9


class Solution:
    def egg_drop(self, k: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][0] = 0
            dp[i][1] = 1

        for j in range(1, n + 1):
            dp[1][j] = j

        for i in range(2, k + 1):  # Количество яиц
            for j in range(2, n + 1):  # Количество этажей
                dp[i][j] = MAX
                for x in range(1, j + 1):  # Перебираем этажи
                    worst = 1 + max(
                        dp[i - 1][x - 1],  # Яйцо разбилось
                        dp[i][j - x],  # Яйцо не разбилось
                    )
                    dp[i][j] = min(dp[i][j], worst)

        return dp[k][n]


class SolutionBinarySearch:
    def egg_drop(self, k: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][0] = 0
            dp[i][1] = 1

        for j in range(1, n + 1):
            dp[1][j] = j

        for i in range(2, k + 1):  # Количество яиц
            for j in range(2, n + 1):  # Количество этажей
                dp[i][j] = MAX
                low = 1
                high = j
                while low <= high:
                    mid = (low + high) // 2
                    break_case = dp[i - 1][mid - 1]  # Яйцо разбилось
                    no_break_case = dp[i][j - mid]  # Яйцо не разбилось
                    worst = 1 + max(break_case, no_break_case)

                    if break_case > no_break_case:
                        high = mid - 1
                    else:
                        low = mid + 1

                    dp[i][j] = min(dp[i][j], worst)

        return dp[k][n]
