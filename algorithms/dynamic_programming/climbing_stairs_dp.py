def climb_stairs_paths(stairs: int) -> int:
    if stairs == 0:
        return 1
    elif stairs == 1:
        return 1

    dp = [0] * (stairs + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, stairs + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[stairs]


def climb_stairs_paths_optimized(stairs: int) -> int:
    if stairs == 0:
        return 1
    elif stairs == 1:
        return 1

    dp1 = 1
    dp2 = 1
    res = None
    for _ in range(2, stairs + 1):
        res = dp1 + dp2

        dp1 = dp2
        dp2 = res

    return res


if __name__ == "__main__":
    print(climb_stairs_paths(10))
    print(climb_stairs_paths_optimized(10))
