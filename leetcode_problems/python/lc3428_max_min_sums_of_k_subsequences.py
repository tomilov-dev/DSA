MIN = 0
MAX = 10**9 + 1
MOD = 10**9 + 7


class SolutionBacktracking:
    def minMaxSums(self, nums: list[int], k: int) -> int:
        def rec(
            i: int,
            depth: int,
            mini: int,
            maxi: int,
        ) -> int:
            if depth >= k:
                return 0
            if i >= n:
                return 0

            mini = min(mini, nums[i])
            maxi = max(maxi, nums[i])
            sub = mini + maxi
            for j in range(i + 1, n):
                sub += rec(j, depth + 1, mini, maxi)
            mini = MAX
            maxi = MIN
            return sub

        total = 0
        n = len(nums)
        for i in range(n):
            total += rec(i, 0, MAX, MIN)
        return total


class SolutionRecursive:
    def minMaxSums(self, nums: list[int], k: int) -> int:
        def rec(i: int, j: int, depth: int) -> int:
            if depth >= k:
                return 0
            if j >= n:
                return 0

            sub = nums[i] + nums[j]
            for jj in range(j + 1, n):
                sub += rec(i, jj, depth + 1)
            return sub

        n = len(nums)
        nums.sort()
        total = 0
        for i in range(n):
            total += rec(i, i, 0)
        return total


class SolutionBottomUp:
    def minMaxSums(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        total = 0

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        # Базовый случай - 1
        for i in range(n + 1):
            dp[i][0] = 1

        # Подсчет количества подпоследовательностей С(n, r)
        for i in range(1, n + 1):
            for j in range(1, min(i + 1, k + 1)):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD

        # Подсчитываем сумму
        for i in range(n):
            for j in range(1, k + 1):
                # Для минимума перемножаем C(i, j - 1) и число
                total = (total + nums[i] * dp[i][j - 1]) % MOD
                # Для максимума перемножаем C(n-i-1, j-1) и число
                total = (total + nums[i] * dp[n - i - 1][j - 1]) % MOD

        return total


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 2
    # nums = [5, 0, 6]
    # k = 1
    # nums = [1, 1, 1]
    # k = 2
    # nums = [1, 0, 1, 2]
    # k = 2
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3
    sol = SolutionBottomUp()
    print(sol.minMaxSums(nums, k))
