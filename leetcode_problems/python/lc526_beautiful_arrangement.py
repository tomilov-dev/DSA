class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(cur: int) -> None:
            nonlocal count
            if cur > n:
                count += 1
                return None

            for i in range(n):
                if stack[i] is not None:
                    continue
                if cur % (i + 1) != 0 and (i + 1) % cur != 0:
                    continue

                stack[i] = cur
                backtrack(cur + 1)
                stack[i] = None

        count = 0
        stack: list[int | None] = [None] * n
        backtrack(1)
        return count


if __name__ == "__main__":
    n = 3
    print(Solution().countArrangement(n))
