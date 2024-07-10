def nSum(n: int) -> int:
    dp = list(range(n + 1))

    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] + i

    return dp[n]


if __name__ == "__main__":
    res = nSum(5)
    print(res)
