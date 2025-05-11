class Solution:
    def printTillN(self, n: int) -> None:
        if n <= 0:
            return None

        self.printTillN(n - 1)
        print(n, end=" ")


class SolutionTailed:
    def printTillN(
        self,
        n: int,
        m: int | None = None,
    ) -> None:
        if m is None:
            m = n - 1
        if m < 0:
            return None

        print(n - m, end=" ")
        self.printTillN(n, m - 1)


if __name__ == "__main__":
    n = 5
    Solution().printTillN(n)
    SolutionTailed().printTillN(n)
