class SolutionRecursive:
    def sum(self, n: int) -> int:
        if n <= 0:
            return 0
        return n + self.sum(n - 1)


class SolutionRecursiveTailed:
    def sum(self, n: int, sm: int = 0) -> int:
        if n <= 0:
            return sm
        return self.sum(n - 1, sm + n)


class SolutionIterative:
    def sum(self, n: int) -> int:
        return sum(i for i in range(1, n + 1))


if __name__ == "__main__":
    n = 5
    print(SolutionRecursive().sum(n))
    print(SolutionRecursiveTailed().sum(n))
    print(SolutionIterative().sum(n))
