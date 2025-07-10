class SolutionRecursive:
    def findMaxSum(self, arr: list[int]) -> int:
        def rec(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return arr[0]
            return max(
                arr[i] + rec(i - 2),
                rec(i - 1),
            )

        return rec(len(arr) - 1)


class SolutionTopDown:
    def findMaxSum(self, arr: list[int]) -> int:
        def rec(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return arr[0]
            if i not in mem:
                mem[i] = max(
                    arr[i] + rec(i - 2),
                    rec(i - 1),
                )
            return mem[i]

        mem = {}
        return rec(len(arr) - 1)


class SolutionBottomUp:
    def findMaxSum(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        dp[1] = arr[0]
        for i in range(2, n + 1):
            dp[i] = max(arr[i - 1] + dp[i - 2], dp[i - 1])
        return dp[n]


class SolutionBottomUpOptimized:
    def findMaxSum(self, arr: list[int]) -> int:
        n = len(arr)
        n1 = 0
        n2 = arr[0]
        for i in range(2, n + 1):
            cur = max(arr[i - 1] + n1, n2)
            n1 = n2
            n2 = cur
        return n2


if __name__ == "__main__":
    arr = [6, 5, 5, 7, 4]
    print(SolutionRecursive().findMaxSum(arr))
    print(SolutionTopDown().findMaxSum(arr))
    print(SolutionBottomUp().findMaxSum(arr))
    print(SolutionBottomUpOptimized().findMaxSum(arr))
