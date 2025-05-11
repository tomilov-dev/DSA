class SolutionRecursive:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    def fibonacciNumbers(self, n: int) -> list[int]:
        return [self.fib(i) for i in range(n)]


class SolutionRecursiveTailed:
    def fib(self, n: int, a: int = 0, b: int = 1) -> int:
        if n == 0:
            return a
        if n == 1:
            return b
        return self.fib(n - 1, b, a + b)

    def fibonacciNumbers(self, n: int) -> list[int]:
        return [self.fib(i) for i in range(n)]


class SolutionRecursiveOptimized:
    def __init__(self) -> None:
        self.mem = {}

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n not in self.mem:
            self.mem[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.mem[n]

    def fibonacciNumbers(self, n: int) -> list[int]:
        return [self.fib(i) for i in range(n)]


class SolutionIterative:
    def fibonacciNumbers(self, n: int) -> list[int]:
        dp = [0] * n
        dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp


if __name__ == "__main__":
    n = 7
    print(SolutionRecursive().fibonacciNumbers(n))
    print(SolutionRecursiveTailed().fibonacciNumbers(n))
    print(SolutionRecursiveOptimized().fibonacciNumbers(n))
    print(SolutionIterative().fibonacciNumbers(n))
