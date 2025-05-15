class Solution:
    def subsets(self, arr: list[int]) -> list[int]:
        def rec(i: int):
            if i >= n:
                return None

            for j in range(i, n):
                if used[j]:
                    continue

                stack.append(arr[j])
                used[j] = True

                res.append(stack[:])
                rec(j + 1)

                stack.pop()
                used[j] = False

        n = len(arr)
        used = [False] * n
        stack = []
        res = [[]]
        rec(0)
        return res


if __name__ == "__main__":
    arr = [1]
    print(Solution().subsets(arr))
