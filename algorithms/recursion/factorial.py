from math import prod


class SolutionRecursive:
    def factorial(self, n: int) -> int:
        if n <= 0:
            return 1
        return n * self.factorial(n - 1)


class SolutionRecursiveTailed:
    def factorial(self, n: int, pr: int = 1) -> int:
        if n <= 0:
            return pr
        return self.factorial(n - 1, pr * n)


class SolutionIterative:
    def factorial(self, n: int) -> int:
        pr = 1
        for i in range(1, n + 1):
            pr *= i
        return pr


class SolutionIterativeOptimized:
    def factorial(self, n: int) -> int:
        return prod(i for i in range(1, n + 1))


if __name__ == "__main__":
    n = 5
    print(SolutionRecursive().factorial(n))
    print(SolutionRecursiveTailed().factorial(n))
    print(SolutionIterative().factorial(n))
    print(SolutionIterativeOptimized().factorial(n))
