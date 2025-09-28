class Solution:
    def champagneTower(
        self,
        poured: int,
        query_row: int,
        query_glass: int,
    ) -> float:
        m = query_glass
        n = query_row
        dp = [[0.0] * (i + 3) for i in range(n + 1)]
        dp[0][1] = poured
        for i in range(1, n + 1):
            for j in range(1, i + 2):
                l = max(dp[i - 1][j] - 1, 0) / 2
                r = max(dp[i - 1][j - 1] - 1, 0) / 2
                dp[i][j] = l + r
        return min(dp[n][m + 1], 1.0)


class SolutionOptimized:
    def champagneTower(
        self,
        poured: int,
        query_row: int,
        query_glass: int,
    ) -> float:
        m = query_glass
        n = query_row
        prev = [0.0] * (n + 3)
        cur = [0.0] * (n + 3)
        prev[1] = poured
        for i in range(1, n + 1):
            for j in range(1, i + 2):
                l = max(prev[j] - 1, 0) / 2
                r = max(prev[j - 1] - 1, 0) / 2
                cur[j] = l + r
            prev, cur = cur, prev
        return min(prev[m + 1], 1.0)


if __name__ == "__main__":
    poured = 1
    query_row = 1
    query_glass = 1

    poured = 2
    query_row = 1
    query_glass = 1

    poured = 100000009
    query_row = 33
    query_glass = 17

    poured = 25
    query_row = 6
    query_glass = 1

    print(SolutionOptimized().champagneTower(poured, query_row, query_glass))
