class SolutionRecursive:
    def arraySum(
        self,
        arr: list[int],
        i: int = 0,
    ) -> int:
        if i >= len(arr):
            return 0
        return arr[i] + self.arraySum(arr, i + 1)


class SolutionRecursiveTailed:
    def arraySum(
        self,
        arr: list[int],
        i: int = 0,
        sm: int = 0,
    ) -> int:
        if i >= len(arr):
            return sm
        return self.arraySum(arr, i + 1, sm + arr[i])


class SolutionIterative:
    def arraySum(self, arr: list[int]) -> int:
        return sum(arr)


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(SolutionRecursive().arraySum(arr))
    print(SolutionRecursiveTailed().arraySum(arr))
    print(SolutionIterative().arraySum(arr))
