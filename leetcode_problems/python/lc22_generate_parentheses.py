class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(n + 1):
            for j in range(i):
                res = ["(" + x + ")" + y for x in dp[j] for y in dp[i - j - 1]]
                dp[i] += res

        return dp[n]


if __name__ == "__main__":
    n = 3
    res = Solution().generateParenthesis(n)
    print(res)
