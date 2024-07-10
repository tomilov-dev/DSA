def climb_stairs_ksteps_paths(stairs: int, k: int) -> int:
    if stairs == 0:
        return 1
    elif stairs == 1:
        return 1

    dp = [0] * (stairs + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, stairs + 1):
        for j in range(1, k + 1):
            if i - j < 0:
                continue

            dp[i] += dp[i - j]

    return dp[stairs]


def climb_stairs_ksteps_paths_optimized(
    stairs: int,
    k: int,
) -> int:
    if stairs == 0:
        return 1
    elif stairs == 1:
        return 1

    dp = [0] * k
    dp[0] = 1

    for i in range(1, stairs + 1):
        for j in range(1, k):
            if i - j < 0:
                continue

            dp[i % k] += dp[(i - j) % k]

    return dp[stairs % k]


def climb_red_stairs_ksteps_paths(
    stairs: int,
    k: int,
    red_stairs: list[bool],
) -> int:
    if stairs == 0:
        return 1
    elif stairs == 1:
        return 1

    dp = [0] * k
    dp[0] = 1

    for i in range(1, stairs + 1):
        for j in range(1, k):
            if i - j < 0:
                continue

            if stairs[i - 1]:
                dp[i % k] = 0
            else:
                dp[i % k] += dp[(i - j) % k]

    return dp[stairs % k]


if __name__ == "__main__":
    # print(climb_stairs_ksteps_paths(10, 2))
    print(climb_stairs_ksteps_paths_optimized(10, 2))
