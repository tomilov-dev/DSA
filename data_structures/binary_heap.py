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


class BinaryHeap:
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

    def heapify(self, index: int):
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
            self.heapify(largest)

    def build(self, array: list[int]) -> None:
        self.storage = [EmptyHeapNode()] + [self.nodify(key) for key in array]
        self.heap_size = len(array)
        for index in range(len(array) // 2, 0, -1):
            self.heapify(index)

    def pop_max(self) -> HeapNode:
        if self.heap_size < 1:
            raise IndexError("The queue is empty")

        max = self.storage[1]
        self.storage[1] = self.storage[self.heap_size]
        self.heap_size -= 1
        self.heapify(1)

        return max

    def empty(self) -> bool:
        return self.heap_size < 1

    def __repr__(self) -> str:
        return f"{self.storage}"


def heapsort(array: list[int]):
    heap = BinaryHeap()
    heap.build(array)

    index = 0
    while not heap.empty():
        array[index] = heap.pop_max()
        index += 1


if __name__ == "__main__":
    array = [50, 20, 14, 6, 10, 45, 5, 4]

    heapsort(array)
    print(array)

    # heap = BinaryHeap()
    # heap.build(array)

    # print(heap.pop_max())

    # heap.sort()
    # print(heap)
