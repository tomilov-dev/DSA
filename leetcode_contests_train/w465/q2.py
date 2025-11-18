class SolutionBacktrackingTLE:
    """TLE"""

    def minDifference(self, n: int, k: int) -> list[int]:
        def score(arr: list[int]) -> int:
            return max(arr) - min(arr)

        def rec(arr: list[int], i: int):
            nonlocal mini
            nonlocal best

            if i >= k - 1:
                return None

            for x in range(1, int(arr[i] ** 0.5) + 1):
                if arr[i] % x != 0:
                    continue

                arr[i] //= x
                arr[i + 1] *= x
                check = score(arr)
                if check <= mini:
                    mini = check
                    best = arr[:]

                if x != 1:
                    rec(arr, i)
                rec(arr, i + 1)

                arr[i] *= x
                arr[i + 1] //= x

        arr = [n] + [1] * (k - 1)
        best = arr[:]
        mini = n
        rec(arr, 0)
        return best


class Solution:
    def __init__(self):
        self.best = []
        self.bestDiff = 10**9

    def backtrack(self, n: int, k: int, start: int, curr: list[int]):
        if k == 1:
            if n >= start:
                curr.append(n)
                self.check(curr)
                curr.pop()
            return

        for i in range(start, n + 1):
            if n % i == 0:
                curr.append(i)
                self.backtrack(n // i, k - 1, i, curr)
                curr.pop()

    def check(self, curr: list[int]):
        diff = max(curr) - min(curr)
        if diff < self.bestDiff:
            self.bestDiff = diff
            self.best = curr[:]

    def minDifference(self, n: int, k: int) -> list[int]:
        self.best = []
        self.bestDiff = 10**9
        self.backtrack(n, k, 1, [])
        return self.best


if __name__ == "__main__":
    n = 100
    k = 2

    # n = 44
    # k = 3

    # n = 360
    # k = 4

    sol = Solution()
    print(sol.minDifference(n, k))
