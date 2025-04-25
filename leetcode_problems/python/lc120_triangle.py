from pprint import pprint


class Solution:
    def minimumTotal(
        self,
        triangle: list[list[int]],
    ) -> int:
        n = len(triangle)
        dp = triangle[-1][:]

        pprint(dp)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
                pprint(dp)

        return dp[0]


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]
    print(Solution().minimumTotal(triangle))
