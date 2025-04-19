class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rowIndex += 1
        dp = [[1] * (i + 1) for i in range(rowIndex)]
        for i in range(2, rowIndex):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp[rowIndex - 1]


class SolutionOptimized:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        dp = [1, 1]
        for i in range(2, rowIndex + 1):
            new = [1] * (i + 1)
            for j in range(1, i):
                new[j] = dp[j - 1] + dp[j]
            dp = new
        return dp


class SolutionSuperOptimized:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                dp[j] += dp[j - 1]
        return dp


if __name__ == "__main__":
    rowIndex = 3
    print(SolutionSuperOptimized().getRow(rowIndex))
