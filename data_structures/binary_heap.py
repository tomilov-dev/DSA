from abc import ABC
from abc import abstractmethod


class AbstractHeapNode:
    key: int


class HeapNode(AbstractHeapNode):
    def __init__(self, key: int) -> None:
        self.key = key

    def __repr__(self) -> str:
        return f"{self.key}"


class EmptyHeapNode(HeapNode):
    def __init__(self) -> None:
        super().__init__(None)


class BaseBinaryHeapOnArray(ABC):
    def __init__(self) -> None:
        self.storage: list[HeapNode] = [EmptyHeapNode()]
        self.heap_size = 0

    def iparent(self, index: int) -> int:
        return index // 2

    def ileft(self, index: int) -> int:
        return 2 * index

    def iright(self, index: int) -> int:
        return 2 * index + 1

    def swap(self, i1: int, i2: int) -> None:
        self.storage[i1], self.storage[i2] = self.storage[i2], self.storage[i1]

    def nodify(self, key: int) -> HeapNode:
        return HeapNode(key)

    def build(self, array: list[int]) -> None:
        self.storage = [EmptyHeapNode()] + [self.nodify(key) for key in array]
        self.heap_size = len(array)
        for index in range(len(array) // 2, 0, -1):
            self.shift_down(index)

    def add(self, value: int) -> None:
        self.storage.append(self.nodify(value))
        self.heap_size += 1
        self.shift_up(self.heap_size)

    def pop(self) -> HeapNode:
        if self.heap_size < 1:
            raise IndexError("The queue is empty")

        max = self.storage[1]
        self.storage[1] = self.storage[self.heap_size]
        self.heap_size -= 1
        self.shift_down(1)

        return max

    @abstractmethod
    def shift_up(self, index: int) -> None:
        pass

    @abstractmethod
    def shift_down(self, index: int) -> None:
        pass

    def empty(self) -> bool:
        return self.heap_size < 1

    def __repr__(self) -> str:
        return f"{self.storage}"


class BinaryMaxHeapOnArray(BaseBinaryHeapOnArray):
    def shift_down(self, index: int) -> None:
        left = self.ileft(index)
        right = self.iright(index)

        largest = index
        if left <= self.heap_size and self.storage[left].key > self.storage[index].key:
            largest = left
        if (
            right <= self.heap_size
            and self.storage[right].key > self.storage[largest].key
        ):
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.shift_down(largest)

    def shift_up(self, index: int) -> None:
        while (
            index > 1
            and self.storage[self.iparent(index)].key < self.storage[index].key
        ):
            self.swap(index, self.iparent(index))
            index = self.iparent(index)


class BinaryHeapOnArray(BaseBinaryHeapOnArray):
    """
    Universal Binary Heap on array. It can be both min and max heap.
    """

    def __init__(
        self,
        is_min_heap: bool = True,
    ):
        super().__init__()
        self.is_min_heap = is_min_heap

    def compare(self, i1: int, i2: int) -> bool:
        if self.is_min_heap:
            return self.storage[i1].key < self.storage[i2].key
        else:
            return self.storage[i1].key > self.storage[i2].key

    def shift_down(self, index: int) -> None:
        left = self.ileft(index)
        right = self.iright(index)

        largest = index
        if left <= self.heap_size and self.compare(left, index):
            largest = left
        if right <= self.heap_size and self.compare(right, largest):
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.shift_down(largest)

    def shift_up(self, index: int) -> None:
        while index > 1 and self.compare(index, self.iparent(index)):
            self.swap(index, self.iparent(index))
            index = self.iparent(index)


def heapsort(array: list[int]):
    heap = BinaryHeapOnArray(is_min_heap=True)
    heap.build(array)

    index = 0
    while not heap.empty():
        array[index] = heap.pop()
        index += 1

    print(array)


if __name__ == "__main__":
    array = [50, 20, 14, 6, 10, 45, 5, 4]

    heapsort(array)

    # heap = BinaryHeapOnArray(is_min_heap=False)
    # heap.build(array)
    # heap.add(60)
    # heap.add(0)

    # print(heap.pop())

    # heap.sort()
    # print(heap)
