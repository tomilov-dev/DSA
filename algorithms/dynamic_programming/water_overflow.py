class Solution:
    def waterOverflow(
        self,
        k: int,
        r: int,
        c: int,
    ) -> float:
        dp = [[0.0] * r for _ in range(r)]
        dp[0][0] = k
        for i in range(r - 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    overflow = dp[i][j] - 1
                    dp[i + 1][j] += overflow / 2
                    dp[i + 1][j + 1] += overflow / 2
        return min(1.0, dp[r - 1][c - 1])


class SolutionOptimized:
    def waterOverflow(
        self,
        k: int,
        r: int,
        c: int,
    ) -> float:
        dp = [0.0] * r
        dp[0] = k
        for i in range(r - 1):
            new_dp = [0.0] * r
            for j in range(i + 1):
                if dp[j] > 1:
                    overflow = dp[j] - 1
                    new_dp[j] += overflow / 2
                    new_dp[j + 1] += overflow / 2
            dp = new_dp
        return min(1.0, dp[c - 1])


if __name__ == "__main__":
    k = 3
    r = 2
    c = 1

    k = 2
    r = 2
    c = 2

    k = 397
    r = 21
    c = 16
    print(Solution().waterOverflow(k, r, c))
    print(SolutionOptimized().waterOverflow(k, r, c))

    # b = 0.5
    # n = b / 0.5
    # print(0.5 * (n // 2 + n % 2))
    # print(0.5 * (n // 2))
