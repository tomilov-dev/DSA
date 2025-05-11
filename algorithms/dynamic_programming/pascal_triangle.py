class SolutionBottomUp:
    def nthRowOfPascalTriangle(self, n: int) -> list[int]:
        dp = [[0] * (n + 2) for _ in range(n)]
        dp[0][1] = 1
        for i in range(1, n):
            for j in range(1, i + 2):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp[-1][1:-1]


class SolutionBottomUpOptimized:
    def nthRowOfPascalTriangle(self, n: int) -> list[int]:
        dp = [0] * (n + 2)
        dp[1] = 1
        for i in range(1, n):
            prev = dp[:]
            for j in range(1, i + 2):
                dp[j] = prev[j - 1] + prev[j]
        return dp[1:-1]


if __name__ == "__main__":
    n = 4
    print(SolutionBottomUp().nthRowOfPascalTriangle(n))
    print(SolutionBottomUpOptimized().nthRowOfPascalTriangle(n))
