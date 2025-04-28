class Solution:
    def minimumTotal(
        self,
        triangle: list[list[int]],
    ) -> int:
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            new_dp = triangle[i]
            for j in range(len(new_dp)):
                new_dp[j] += min(dp[j], dp[j + 1])
            dp = new_dp
        return max(dp)


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution().minimumTotal(triangle))
