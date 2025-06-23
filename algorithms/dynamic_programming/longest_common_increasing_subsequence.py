class SolutionRecursive:
    def lcis(self, left: list[int], right: list[int]) -> int:
        def rec(i: int, j: int, p: int | None = None) -> int:
            if i >= m or j >= n:
                return 0

            take = 0
            if (p is None or left[p] < left[i]) and left[i] == right[j]:
                take = 1 + rec(i + 1, j + 1, i)

            not_take = max(rec(i + 1, j, p), rec(i, j + 1, p))
            return max(take, not_take)

        m = len(left)
        n = len(right)
        return rec(0, 0)


class SolutionTopDown:
    def lcis(self, left: list[int], right: list[int]) -> int:
        def rec(i: int, j: int, p: int | None = None) -> int:
            if i >= m or j >= n:
                return 0

            key = (i, j, p)
            if key not in mem:
                take = 0
                if (p is None or left[p] < left[i]) and left[i] == right[j]:
                    take = 1 + rec(i + 1, j + 1, i)

                not_take = max(rec(i + 1, j, p), rec(i, j + 1, p))
                mem[key] = max(take, not_take)
            return mem[key]

        m = len(left)
        n = len(right)
        mem = {}
        return rec(0, 0)


class SolutionBottomUp:
    def lcis(self, left: list[int], right: list[int]) -> int:
        m = len(left)
        n = len(right)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if left[i - 1] == right[j - 1]:
                    max_prev = 0
                    for k in range(1, j):
                        if right[k - 1] < right[j - 1]:
                            max_prev = max(max_prev, dp[i - 1][k])
                    dp[i][j] = max(dp[i][j], max_prev + 1)

        return max(dp[m])


class SolutionBottomUpOptimized:
    def lcis(self, left: list[int], right: list[int]) -> int:
        m = len(left)
        n = len(right)
        dp = [0] * n

        for i in range(m):
            cur_max = 0
            for j in range(n):
                if left[i] == right[j]:
                    dp[j] = max(dp[j], cur_max + 1)
                elif left[i] > right[j]:
                    cur_max = max(cur_max, dp[j])
        return max(dp)


if __name__ == "__main__":
    a = [3, 4, 9, 1]
    b = [5, 3, 8, 9, 10, 2, 1]

    a = [1, 1, 4, 3]
    b = [1, 1, 3, 4]
    print(SolutionRecursive().lcis(a, b))
    print(SolutionTopDown().lcis(a, b))
    print(SolutionBottomUp().lcis(a, b))
    print(SolutionBottomUpOptimized().lcis(a, b))
