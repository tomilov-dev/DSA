from functools import lru_cache
from collections import deque
from collections import defaultdict


MOD = 10**9 + 7


class SolutionBacktracking:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        def backtrack(k: int):
            if k == 0:
                results.append(stack[:])
                return None

            for num in range(l, r + 1):
                if stack[-1] == num:
                    continue
                if len(stack) >= 2 and stack[-2] > stack[-1] > num:
                    continue
                if len(stack) >= 2 and stack[-2] < stack[-1] < num:
                    continue

                stack.append(num)
                backtrack(k - 1)
                stack.pop()

        results = []
        stack: list[int] = []
        for num in range(l, r + 1):
            stack.append(num)
            backtrack(n - 1)
            stack.pop()

        return len(results) % MOD


class SolutionMemoization:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        def backtrack(i: int, prev1: int, prev2: int) -> int:
            if i == n:
                return 1

            key = (i, prev1, prev2)
            if key not in mem:
                total = 0
                for num in range(l, r + 1):
                    if num == prev1:
                        continue
                    if i >= 2 and prev2 < prev1 < num:
                        continue
                    if i >= 2 and prev2 > prev1 > num:
                        continue
                    total = (total + backtrack(i + 1, num, prev1)) % MOD
                mem[key] = total
            return mem[key]

        mem = {}
        result = 0
        for num in range(l, r + 1):
            result = (result + backtrack(1, num, -1)) % MOD
        return result


class SolutionMemoizationLRU:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        @lru_cache(maxsize=None)
        def backtrack(i: int, prev1: int, prev2: int) -> int:
            if i == n:
                return 1

            total = 0
            for num in range(l, r + 1):
                if num == prev1:
                    continue
                if i >= 2 and prev2 < prev1 < num:
                    continue
                if i >= 2 and prev2 > prev1 > num:
                    continue
                total = (total + backtrack(i + 1, num, prev1)) % MOD
            return total

        result = 0
        for num in range(l, r + 1):
            result = (result + backtrack(1, num, -1)) % MOD
        return result


class SolutionQueueMemoization:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mem = defaultdict(int)
        queue = deque()

        for num in range(l, r + 1):
            mem[(1, num, -1)] = 1
            queue.append((1, num, -1))

        while queue:
            i, prev1, prev2 = queue.popleft()
            if i == n:
                continue

            for num in range(l, r + 1):
                if num == prev1:
                    continue
                if i >= 2 and prev2 < prev1 < num:
                    continue
                if i >= 2 and prev2 > prev1 > num:
                    continue

                key = (i + 1, num, prev1)
                if mem[key] == 0:
                    queue.append((i + 1, num, prev1))
                mem[key] = (mem[key] + mem[(i, prev1, prev2)]) % MOD

        result = 0
        for (i, prev1, prev2), count in mem.items():
            if i == n:
                result = (result + count) % MOD
        return result


class SolutionBottomUp:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        values = list(range(l, r + 1))
        size = len(values)

        dp = [[[0 for _ in range(size + 1)] for _ in range(size)] for _ in range(n + 1)]
        for i, v in enumerate(values):
            dp[1][i][size] = 1

        for i in range(1, n):
            for prev1 in range(size):
                for prev2 in range(size + 1):
                    count = dp[i][prev1][prev2]
                    if count == 0:
                        continue

                    for nxt in range(size):
                        if nxt == prev1:
                            continue
                        if i >= 2 and prev2 != size:
                            a, b, c = values[prev2], values[prev1], values[nxt]
                            if a < b < c or a > b > c:
                                continue
                        dp[i + 1][nxt][prev1] = (dp[i + 1][nxt][prev1] + count) % MOD

        result = 0
        for prev1 in range(size):
            for prev2 in range(size + 1):
                result = (result + dp[n][prev1][prev2]) % MOD
        return result


if __name__ == "__main__":
    n = 3
    l = 4
    r = 5

    n = 3
    l = 1
    r = 3

    n = 4
    l = 3
    r = 5

    n = 14
    l = 71
    r = 166

    import time

    start = time.time()
    print(SolutionBottomUp().zigZagArrays(n, l, r))
    print("Duration:", time.time() - start, "sec.")
