class SolutionRecursive:
    def min(self, arr: list[int], i: int = 0) -> int:
        if i >= len(arr) - 1:
            return arr[0]
        return min(arr[i], self.min(arr, i + 1))

    def max(self, arr: list[int], i: int = 0) -> int:
        if i >= len(arr) - 1:
            return arr[0]
        return max(arr[i], self.max(arr, i + 1))

    def extreme(self, arr: list[int]) -> tuple[int, int]:
        return self.min(arr), self.max(arr)


class SolutionRecursiveTailed:
    def min(
        self,
        arr: list[int],
        i: int = 0,
        t: int = 10**6,
    ) -> int:
        if i >= len(arr):
            return t
        return self.min(arr, i + 1, min(arr[i], t))

    def max(
        self,
        arr: list[int],
        i: int = 0,
        t: int = -(10**6),
    ) -> int:
        if i >= len(arr):
            return t
        return self.max(arr, i + 1, max(arr[i], t))

    def extreme(self, arr: list[int]) -> tuple[int, int]:
        return self.min(arr), self.max(arr)


class SolutionIterative:
    def extreme(self, arr: list[int]) -> tuple[int, int]:
        return min(arr), max(arr)


if __name__ == "__main__":
    arr = [1, 4, 3, -5, -4, 8, 6]
    print(SolutionRecursive().extreme(arr))
    print(SolutionRecursiveTailed().extreme(arr))
    print(SolutionIterative().extreme(arr))
