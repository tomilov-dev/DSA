class SolutionBacktracking:
    def findPermutation(self, s: str) -> list[str]:
        def rec() -> None:
            if len(stack) == n:
                res.append("".join(stack))
                return None

            for j in range(0, n):
                if used[j]:
                    continue

                used[j] = True
                stack.append(s[j])
                rec()
                stack.pop()
                used[j] = False

        n = len(s)
        s = sorted(s)  # type:ignore
        used = [False] * n
        stack = []
        res = []
        rec()
        return sorted(set(res))


class SolutionBacktrackingOptimized:
    def findPermutation(self, s: str) -> list[str]:
        def rec() -> None:
            if len(stack) == n:
                res.append("".join(stack))
                return None

            for j in range(0, n):
                if used[j]:
                    continue
                if j > 0 and s[j] == s[j - 1] and not used[j - 1]:
                    continue

                used[j] = True
                stack.append(s[j])
                rec()
                stack.pop()
                used[j] = False

        n = len(s)
        s = sorted(s)  # type:ignore
        used = [False] * n
        stack = []
        res = []
        rec()
        return res


if __name__ == "__main__":
    s = "abc"
    s = "kk"
    print(SolutionBacktracking().findPermutation(s))
