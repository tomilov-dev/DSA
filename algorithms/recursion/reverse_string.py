class SolutionRecursive:
    def reverseString(self, s: str) -> str:
        if len(s) == 1:
            return s
        return self.reverseString(s[1:]) + s[0]


class SolutionRecursiveTailed:
    def reverse(
        self,
        s: list[str],
        q: list[str],
        i: int,
    ) -> list[str]:
        if i >= len(s):
            return q
        q[len(s) - i - 1] = s[i]
        return self.reverse(s, q, i + 1)

    def reverseString(self, s: str) -> str:
        return "".join(self.reverse(list(s), [""] * len(s), 0))


class SolutionIterative:
    def reverseString(self, s: str) -> str:
        q = list(s)
        for i in range(0, len(s) // 2):
            j = len(q) - i - 1
            q[i], q[j] = q[j], q[i]
        return "".join(q)


if __name__ == "__main__":
    s = "Geeks for Geeks"
    print(SolutionRecursive().reverseString(s))
    print(SolutionRecursiveTailed().reverseString(s))
    print(SolutionIterative().reverseString(s))
