class SolutionRecursive:
    def sum(self, d: int) -> int:
        if d <= 0:
            return 0
        return d % 10 + self.sum(d // 10)


class SolutionRecursiveTailed:
    def sum(self, d: int, sm: int = 0) -> int:
        if d <= 0:
            return sm
        return self.sum(d // 10, sm + d % 10)


class SolutionIterative:
    def sum(self, d: int) -> int:
        sm = 0
        while d > 0:
            sm += d % 10
            d //= 10
        return sm


if __name__ == "__main__":
    d = 12345
    print(SolutionRecursive().sum(d))
    print(SolutionRecursiveTailed().sum(d))
    print(SolutionIterative().sum(d))
