class Solution:
    def combine(
        self,
        n: int,
        k: int,
    ) -> list[list[int]]:
        def backtrack(i: int) -> None:
            if len(stack) == k:
                res.append(stack[:])
                return None

            for j in range(i, n + 1):
                if len(stack) + (n - j + 1) < k:
                    break

                stack.append(j)
                backtrack(j + 1)
                stack.pop()

        res = []
        stack = []
        backtrack(1)
        return res


if __name__ == "__main__":
    n = 4
    k = 2
    print(Solution().combine(n, k))
