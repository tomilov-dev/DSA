def cut_rod_rec(p: list[int], n: int) -> int:
    if n == 0:
        return 0

    q = float("-inf")
    for i in range(n):
        q = max(q, p[i] + cut_rod_rec(p, n - i - 1))

    return q


def top_down_helper(p: list[int], n: int, dp: list[int]) -> int:
    if dp[n] != float("-inf"):
        return dp[n]
    if n == 0:
        q = 0
    else:
        q = float("-inf")
        for i in range(n):
            q = max(q, p[i] + top_down_helper(p, n - i - 1, dp))

    dp[n] = q
    return q


def cut_rod_top_down(p: list[int], n: int) -> int:
    dp = [float("-inf")] * (n + 1)
    return top_down_helper(p, n, dp)


def cut_rod_bottom_up(p: list[int], n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        q = float("-inf")
        for j in range(i):
            q = max(q, p[j] + dp[i - j - 1])
        dp[i] = q

    return dp[n]


if __name__ == "__main__":
    p = [1, 5, 8, 9]
    n = 4

    print(cut_rod_rec(p, n))
    print(cut_rod_top_down(p, n))
    print(cut_rod_bottom_up(p, n))
