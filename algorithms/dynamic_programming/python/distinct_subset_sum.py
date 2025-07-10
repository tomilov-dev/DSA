class SolutionRecursive:
    def sums(self, arr: list[int]) -> list[int]:
        def rec(i: int, sm: int = 0) -> None:
            if i == len(arr):
                # Не нужна проверка - set не содержит дубликатов
                res.add(sm)
                return

            rec(i + 1, sm + arr[i])
            rec(i + 1, sm)

        res = set()
        rec(0)
        return sorted(res)


class SolutionTopDown:
    def sums(self, arr: list[int]) -> list[int]:
        def rec(i: int, sm: int = 0) -> None:
            if i == len(arr):
                # Не нужна проверка - set не содержит дубликатов
                res.add(sm)
                return

            key = (i, sm)
            if key in mem:
                return None

            mem.add(key)
            rec(i + 1, sm + arr[i])
            rec(i + 1, sm)

        res = set()
        mem = set()
        rec(0)
        return sorted(res)


class SolutionBottomUp:
    def sums(self, arr: list[int]) -> list[int]:
        n = sum(arr)
        dp = [False] * (n + 1)
        dp[0] = True
        for num in arr:
            for s in range(n, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        return [i for i, v in enumerate(dp) if v]


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(SolutionRecursive().sums(arr))
    print(SolutionTopDown().sums(arr))
    print(SolutionBottomUp().sums(arr))
