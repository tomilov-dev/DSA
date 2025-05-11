class SolutionRecursiveTailed:
    def sum(
        self,
        arr: list[int],
        i: int = 0,
        sm: int = 0,
    ) -> int:
        if i >= len(arr):
            return sm
        return self.sum(arr, i + 1, sm + arr[i])

    def mean(self, arr: list[int]) -> float:
        arr_sum = self.sum(arr, 0)
        return arr_sum / len(arr)


class SolutionIterative:
    def mean(self, arr: list[int]) -> float:
        return sum(arr) / len(arr)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(SolutionRecursiveTailed().mean(arr))
    print(SolutionIterative().mean(arr))
