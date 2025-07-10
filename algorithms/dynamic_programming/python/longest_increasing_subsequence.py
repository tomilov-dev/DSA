import bisect


class SolutionRecursive:
    def lis(self, arr: list[int]) -> int:
        def rec(i: int) -> int:
            if i == n:
                return 0

            maxi = 1  # it is must have value because handle corners
            for j in range(i):
                if arr[j] < arr[i]:
                    maxi = max(maxi, rec(j) + 1)
            return maxi

        n = len(arr)
        lis = 1  # Default value if len(arr) != 0
        for i in range(1, n):
            lis = max(lis, rec(i))
        return lis


class SolutionRecursiveOptimized:
    def lis(self, arr: list[int]) -> int:
        def rec(i: int, prev: int) -> int:
            if i == len(arr):
                return 0

            take = 0
            if prev == -1 or arr[i] > arr[prev]:
                take = 1 + rec(i + 1, i)
            not_take = rec(i + 1, prev)
            return max(take, not_take)

        return rec(0, -1)


class SolutionTopDown:
    def lis(self, arr: list[int]) -> int:
        def rec(i: int, prev: int) -> int:
            if i == len(arr):
                return 0

            key = (i, prev)
            if key not in mem:
                take = 0
                if prev == -1 or arr[i] > arr[prev]:
                    take = 1 + rec(i + 1, i)
                not_take = rec(i + 1, prev)
                mem[key] = max(take, not_take)
            return mem[key]

        mem = dict()
        return rec(0, -1)


class SolutionBottomUp:
    def lis(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class SolutionBottomUpOptimizedBinarySearch:
    def lis(self, arr: list[int]) -> int:
        sub = []
        for num in arr:
            pos = bisect.bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        return len(sub)


if __name__ == "__main__":
    arr = [5, 8, 3, 7, 9, 1]
    # arr = [48, 37, 41, 38, 2]
    print(SolutionRecursive().lis(arr))
    print(SolutionRecursiveOptimized().lis(arr))
    print(SolutionTopDown().lis(arr))
    print(SolutionBottomUp().lis(arr))
    print(SolutionBottomUpOptimizedBinarySearch().lis(arr))
