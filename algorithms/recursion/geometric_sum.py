class SolutionRecursive:
    def calc(self, n: int) -> int:
        if n == 0:
            return 1
        return 1 / (3**n) + self.calc(n - 1)


if __name__ == "__main__":
    n = 5
    print(SolutionRecursive().calc(n))
