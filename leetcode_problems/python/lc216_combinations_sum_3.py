class Solution:
    def combinationSum3(
        self,
        k: int,
        n: int,
    ) -> list[list[int]]:
        def backtrack(i: int, cursum: int) -> None:
            if cursum == n and len(stack) == k:
                res.append(stack[:])
                return None
            elif cursum > n:
                return None
            elif len(stack) > k:
                return None

            for j in range(i, z + 1):
                cursum += j
                stack.append(j)
                backtrack(j + 1, cursum)
                stack.pop()
                cursum -= j

        z = min(9, n)
        res = []
        stack = []
        backtrack(1, 0)
        return res


if __name__ == "__main__":
    k = 3
    n = 7

    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))
