from collections import deque


class Solution:
    def numsSameConsecDiff(
        self,
        n: int,
        k: int,
    ) -> list[int]:
        def to_num(arr: list[int]) -> int:
            numb = 0
            i = len(arr) - 1
            for num in arr:
                numb += num * 10**i
                i -= 1
            return numb

        def backtrack() -> None:
            if len(stack) == n:
                res.append(to_num(stack))
                return None

            for i in range(10):
                if not stack and i == 0:
                    continue

                if not stack or abs(stack[-1] - i) == k:
                    stack.append(i)
                    backtrack()
                    stack.pop()

        stack = []
        res = []
        backtrack()
        return res


class Solution2:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        def dfs(num, length):
            if length == n:
                res.append(num)
                return
            last_digit = num % 10
            next_digits = set([last_digit + k, last_digit - k])
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    dfs(num * 10 + next_digit, length + 1)

        res = []
        for i in range(1, 10):
            dfs(i, 1)
        return res


class SolutionQueue:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        if n == 1:
            return [i for i in range(10)]

        queue = deque([i for i in range(1, 10)])
        for _ in range(n - 1):
            size = len(queue)
            for _ in range(size):
                num = queue.popleft()
                last_digit = num % 10
                next_digits = set([last_digit + k, last_digit - k])
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        queue.append(num * 10 + next_digit)

        return list(queue)


if __name__ == "__main__":
    n = 3
    k = 7

    # n = 2
    # k = 0
    print(Solution().numsSameConsecDiff(n, k))
