import random
from abc import ABC
from abc import abstractmethod


class Sorter(ABC):
    @abstractmethod
    def sort(
        self,
        array: list[int],
    ) -> None:
        pass


class ClassicQuickSort(Sorter):
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


class QuickSort(Sorter):
    def get_pivot(
        self,
        array: list[int],
        l: int,
        r: int,
    ) -> tuple[int, int]:
        return array[r], r

    def partition(
        self,
        array: list[int],
        l: int,
        r: int,
    ) -> int:
        pivot, pivot_index = self.get_pivot(array, l, r)
        array[pivot_index], array[r] = array[r], array[pivot_index]

        p1 = l
        p2 = r - 1
        while p1 <= p2:
            if array[p1] < pivot:
                p1 += 1
            elif array[p2] > pivot:
                p2 -= 1
            else:
                array[p1], array[p2] = array[p2], array[p1]
                p1 += 1
                p2 -= 1

        array[p1], array[r] = array[r], array[p1]
        return p1

    def qsort(
        self,
        array: list[int],
        l: int,
        r: int,
    ) -> None:
        if l >= r:
            return None

        ip = self.partition(array, l, r)
        self.qsort(array, l, ip - 1)
        self.qsort(array, ip + 1, r)

    def sort(
        self,
        array: list[int],
    ) -> None:
        self.qsort(array, 0, len(array) - 1)


def test_it(sorter: Sorter):
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 3, 3, 1], [1, 1, 2, 3, 3, 3]),
        ([0, -1, 3, -2, 2, 1], [-2, -1, 0, 1, 2, 3]),
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
    ]

    for i, (input_array, expected_output) in enumerate(test_cases):
        sorter.sort(input_array)
        assert (
            input_array == expected_output
        ), f"Test case {i + 1} failed: {input_array} != {expected_output}"
        print(f"Test case {i + 1} passed")

    print("All test cases passed")


if __name__ == "__main__":
    array = [4, 3, 2, 1]

    # sorter1 = ClassicQuickSort()
    # sorter1.sort(array, 0, len(array) - 1)

    # sorter2 = ClassicQuickSortRandomize()
    # sorter2.sort(array, 0, len(array) - 1)

    # sorter3 = QuickSortRandom()
    # sorter3.sort(array)

    sorter4 = QuickSort()
    sorter4.sort(array)

    test_it(sorter4)
