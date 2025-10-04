class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        n = numRows
        dp = [[0] * (i + 3) for i in range(n)]
        dp[0][1] = 1
        for i in range(1, n):
            for j in range(1, i + 2):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return [row[1:-1] for row in dp]


class SolutionWithoutBorders:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp


class SolutionOptimized:
    def getValue(self, row: int, col: int) -> int:
        if col == 0 or col == row:
            return 1

        prev = [1] * (row + 1)
        curr = [1] * (row + 1)
        for i in range(1, row + 1):
            for j in range(1, i):
                curr[j] = prev[j - 1] + prev[j]
            prev, curr = curr, prev

        return prev[col]


class SolutionSuperOptimized:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = [1] * (rowIndex + 1)

        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                dp[j] += dp[j - 1]

        return dp
