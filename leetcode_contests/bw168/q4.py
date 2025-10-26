import math
from functools import reduce
from collections import Counter


MOD = 10**9 + 7


class Solution:
    def countCoprime(self, mat: list[list[int]]) -> int:
        def rec(i: int) -> None:
            nonlocal res
            if i >= m:
                if reduce(math.gcd, stack) == 1:
                    res += 1
                return None

            for j in range(n):
                stack.append(mat[i][j])
                rec(i + 1)
                stack.pop()

        m = len(mat)
        n = len(mat[0])
        stack = []
        res = 0
        rec(0)
        return res % MOD


if __name__ == "__main__":

    mat = [[1, 2], [3, 4]]
    mat = [[2, 2], [2, 2]]
    sol = Solution()
    print(sol.countCoprime(mat))
