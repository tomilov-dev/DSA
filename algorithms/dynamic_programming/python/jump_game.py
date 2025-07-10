MAX = 10**6


class SolutionRecursive:
    def minJumps(self, arr: list[int]) -> int:
        def rec(i: int, c: int) -> int:
            if i == len(arr) - 1:
                return c
            if i >= len(arr):
                return MAX

            MIN = MAX
            for j in range(1, arr[i] + 1):
                MIN = min(MIN, rec(i + j, c + 1))
            return MIN

        res = rec(0, 0)
        return -1 if res == MAX else res


class SolutionTopDown:
    def minJumps(self, arr: list[int]) -> int:
        def rec(i: int, c: int) -> int:
            if i == len(arr) - 1:
                return c
            if i >= len(arr):
                return MAX

            key = (i, c)
            if key not in mem:
                MIN = MAX
                for j in range(1, arr[i] + 1):
                    MIN = min(MIN, rec(i + j, c + 1))
                mem[key] = MIN
            return mem[key]

        mem = {}
        res = rec(0, 0)
        return -1 if res == MAX else res


class SolutionBottomUp:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [MAX] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, arr[i] + 1):
                if i + j >= n:
                    continue
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return -1 if dp[n - 1] == MAX else dp[n - 1]


if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    arr = [1, 4, 3, 2, 6, 7]
    # arr = [0, 10, 20]
    print(SolutionRecursive().minJumps(arr))
    print(SolutionTopDown().minJumps(arr))
    print(SolutionBottomUp().minJumps(arr))
