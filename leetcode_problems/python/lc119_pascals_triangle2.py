class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rowIndex += 1
        if rowIndex == 1:
            return [1]

        dp = [[]] * rowIndex
        dp[0] = [1]

        for i in range(1, rowIndex):
            local = [0] * (i + 1)
            for j in range(len(local)):
                if j == 0 or j == i:
                    local[j] = 1
                else:
                    local[j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp[i] = local

        return dp[-1]


if __name__ == "__main__":
    rowIndex = 3
    print(Solution().getRow(rowIndex))
