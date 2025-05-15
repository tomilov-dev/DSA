class SolutionRecursive:
    def longest(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if s[0] == s[-1]:
            return 2 + self.longest(s[1:-1])
        return max(self.longest(s[1:]), self.longest(s[:-1]))


class SolutionRecursiveOptimized:
    def longest(self, s: str) -> int:
        def rec(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + rec(i + 1, j - 1)
            return max(rec(i + 1, j), rec(i, j - 1))

        return rec(0, len(s) - 1)


class SolutionTopDown:
    def longest(self, s: str) -> int:
        def rec(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1

            key = (i, j)
            if key not in mem:
                if s[i] == s[j]:
                    mem[key] = 2 + rec(i + 1, j - 1)
                else:
                    mem[key] = max(rec(i + 1, j), rec(i, j - 1))
            return mem[key]

        mem = {}
        return rec(0, len(s) - 1)


if __name__ == "__main__":
    s = "banana"
    s = "aaaabbaa"
    print(SolutionRecursive().longest(s))
    print(SolutionRecursiveOptimized().longest(s))
    print(SolutionTopDown().longest(s))
