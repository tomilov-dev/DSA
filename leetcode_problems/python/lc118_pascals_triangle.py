class Solution:
    def generate(
        self,
        numRows: int,
    ) -> list[list[int]]:
        dp = [[0] * (i + 3) for i in range(numRows)]
        dp[0][1] = 1
        for i in range(1, numRows):
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return [sub[1:-1] for sub in dp]


class SolutionOptimized:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = [[1] * (i + 1) for i in range(numRows)]
        ## dp[0] && dp[1] initialized like [1], [1, 1]
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp


if __name__ == "__main__":
    numRows = 5
    print(SolutionOptimized().generate(numRows))
