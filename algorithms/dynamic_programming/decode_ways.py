class Solution:
    def countWays(self, digits: str) -> int:
        n = len(digits)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if digits[i] != "0":
                dp[i + 1] += dp[i]
            if digits[i - 1] != "0" and int(digits[i - 1 : i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[n]


if __name__ == "__main__":
    digits = "123"
    print(Solution().countWays(digits))
