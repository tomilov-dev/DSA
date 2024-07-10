def min_cost(n: int, p: list[int]) -> int:
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = p[1]

    for i in range(2, n + 1):
        dp[i] = p[i] + min(dp[i - 1], dp[i - 2])

    return dp[n]


def reverse(path: list[int]) -> list[int]:
    i = 0
    j = len(path) - 1
    while i < j:
        path[i], path[j] = path[j], path[i]

        i += 1
        j -= 1

    return path


def min_cost_path(n: int, p: list[int]) -> list[int]:
    dp = [0] * (n + 1)
    dfrom = [0] * (n + 1)

    dp[0] = 0
    dp[1] = p[1]

    for i in range(2, n + 1):
        if dp[i - 1] < dp[i - 2]:
            dfrom[i] = i - 1
        else:
            dfrom[i] = i - 2

        dp[i] = p[i] + min(dp[i - 1], dp[i - 2])

    path: list[int] = []
    curr = n
    while curr >= 0:
        path.append(curr)
        if curr == 0:
            break

        curr = dfrom[curr]

    return reverse(path)


if __name__ == "__main__":
    print(min_cost(3, [0, 3, 2, 4]))
    print(min_cost_path(3, [0, 3, 2, 4]))
