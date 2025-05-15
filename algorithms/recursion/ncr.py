class SolutionRecursive:
    def ncr(self, n: int, r: int) -> int:
        if n < r:
            return 0
        if r == 1:
            return n
        if n == 1 or r == 0:
            return 1
        return self.ncr(n - 1, r - 1) + self.ncr(n - 1, r)


class SolutionTopDown:
    def ncr(self, n: int, r: int) -> int:
        def rec(n: int, r: int) -> int:
            if n < r:
                return 0
            if r == 1:
                return n
            if n == 1 or r == 0:
                return 1
            key = (n, r)
            if key not in mem:
                mem[key] = self.ncr(n - 1, r - 1) + self.ncr(n - 1, r)
            return mem[key]

        mem = {}
        return rec(n, r)


if __name__ == "__main__":
    n = 5
    r = 2
    print(SolutionRecursive().ncr(n, r))
    print(SolutionTopDown().ncr(n, r))
