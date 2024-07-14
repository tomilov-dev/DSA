class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [1]

        dp = [[]] * numRows
        dp[0] = [1]

        for i in range(1, numRows):
            local = [0] * (i + 1)
            for j in range(len(local)):
                if j == 0 or j == i:
                    local[j] = 1
                else:
                    local[j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp[i] = local

        return dp


if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))
