import random


class ClassicQuickSort:
    def partition(
        self,
        array: list[int],
        start: int,
        end: int,
    ) -> int:
        x = array[end]
        i = start - 1
        for j in range(start, end):
            if array[j] <= x:
                i = i + 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[end] = array[end], array[i + 1]
        return i + 1

    def _partition(
        self,
        array: list[int],
        start: int,
        end: int,
    ) -> int:
        x = array[end]
        i = start
        for j in range(start, end):
            if array[j] <= x:
                array[i], array[j] = array[j], array[i]
                i = i + 1
        array[i], array[end] = array[end], array[i]
        return i

    def sort(
        self,
        array: list[int],
        start: int,
        end: int,
    ) -> None:
        if start >= end:
            return

        q = self._partition(array, start, end)
        self.sort(array, start, q - 1)
        self.sort(array, q + 1, end)


class ClassicQuickSortRandomize(ClassicQuickSort):
    def randomized_partition(
        self,
        array: list[int],
        start: int,
        end: int,
    ):
        i = random.choice(range(start, end))
        array[end], array[i] = array[i], array[end]
        return self.partition(array, start, end)

    def sort(
        self,
        array: list[int],
        start: int,
        end: int,
    ) -> None:
        if start >= end:
            return

        q = self.randomized_partition(array, start, end)
        self.sort(array, start, q - 1)
        self.sort(array, q + 1, end)


class QuickSortRandom:
    def partition(
        self,
        array: list[int],
        pivot: int,
    ) -> tuple[list[int], list[int], list[int]]:
        less = [i for i in array if i < pivot]
        center = [i for i in array if i == pivot]
        greater = [i for i in array if i > pivot]
        return less, center, greater

    def sort(self, array: list[int]) -> list[int]:
        if len(array) < 2:
            return array
        else:
            pivot = random.choice(array)
            less, center, greater = self.partition(array, pivot)
            return self.sort(less) + center + self.sort(greater)


if __name__ == "__main__":
    array = [4, 3, 2, 1]

    sorter1 = ClassicQuickSort()
    sorter1.sort(array, 0, len(array) - 1)

    # sorter2 = ClassicQuickSortRandomize()
    # sorter2.sort(array, 0, len(array) - 1)

    # sorter3 = QuickSortRandom()
    # sorter3.sort(array)

    print(array)
