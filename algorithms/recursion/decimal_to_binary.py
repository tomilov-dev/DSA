class SolutionRecursive:
    def convert(self, n: int) -> int:
        if n == 0:
            return 0
        return n % 2 + 10 * self.convert(n // 2)


class SolutionRecursiveTailed:
    def convert(
        self,
        n: int,
        b: int = 0,
        m: int = 1,
    ) -> int:
        if n == 0:
            return b
        return self.convert(
            n // 2,
            b + (n % 2) * m,
            m * 10,
        )


if __name__ == "__main__":
    n = 7
    print(SolutionRecursive().convert(n))
    print(SolutionRecursiveTailed().convert(n))
