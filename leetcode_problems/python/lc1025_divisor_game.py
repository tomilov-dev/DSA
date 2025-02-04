class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        if n >= 1:
            dp[1] = False
        if n >= 2:
            dp[2] = True

        for i in range(3, n + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break

        return dp[n]


if __name__ == "__main__":
    n = 3
    print(Solution().divisorGame(n))
