class SolutionRecursive:
    def fibonacci(self, n: int, a: int, b: int) -> None:
        if n > 0:
            self.fibonacci(n - 1, b, a + b)
            print(a, end=" ")


if __name__ == "__main__":
    n = 5
    SolutionRecursive().fibonacci(n, 0, 1)
