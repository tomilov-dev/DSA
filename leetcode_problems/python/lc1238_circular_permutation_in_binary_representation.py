class Solution:
    def circularPermutation(
        self,
        n: int,
        start: int,
    ) -> list[int]:
        def generate_neighbors(num: int) -> list[int]:
            nb = []
            for i in range(n):
                nb.append(num ^ (1 << i))
            return nb

        def is_valid(cur: int, prev: int) -> bool:
            xor = cur ^ prev
            return xor > 0 and (xor & (xor - 1)) == 0

        def backtrack(i: int) -> bool:
            if i >= k:
                return is_valid(stack[0], stack[-1])

            for j in nb[stack[i - 1]]:
                if used[j] or not is_valid(j, stack[i - 1]):
                    continue

                used[j] = True
                stack[i] = j
                if backtrack(i + 1):
                    return True
                stack[i] = -1
                used[j] = False

            return False

        k = 2**n
        used = [False] * k
        used[start] = True
        stack = [-1] * k
        stack[0] = start

        nb = {i: generate_neighbors(i) for i in range(k)}

        backtrack(1)
        return stack


if __name__ == "__main__":
    n = 2
    start = 3
    print(Solution().circularPermutation(n, start))
