class AbstractQueueNode:
    key: int


class QueueNode(AbstractQueueNode):
    def __init__(self, key: int) -> None:
        self.key = key

    def __repr__(self) -> str:
        return f"{self.key}"


class EmptyQueueNode(QueueNode):
    def __init__(self) -> None:
        super().__init__(None)


class PriorityQueue:
    def __init__(self) -> None:
        self.queue: list[QueueNode] = [EmptyQueueNode()]
        self.queue_size = 0

    def iparent(self, index: int) -> int:
        return index // 2

    def ileft(self, index: int) -> int:
        return 2 * index

    def iright(self, index: int) -> int:
        return 2 * index + 1

    def swap(self, i1: int, i2: int) -> None:
        self.queue[i1], self.queue[i2] = self.queue[i2], self.queue[i1]

    def nodify(self, key: int) -> QueueNode:
        return QueueNode(key)

    def heapify(self, index: int):
        left = self.ileft(index)
        right = self.iright(index)

        largest = index
        if left <= self.queue_size and self.queue[left].key > self.queue[index].key:
            largest = left
        if right <= self.queue_size and self.queue[right].key > self.queue[largest].key:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.heapify(largest)

    def build(self, array: list[int]) -> None:
        self.queue = [EmptyQueueNode()] + [self.nodify(key) for key in array]
        self.queue_size = len(array)
        for index in range(len(array) // 2, 0, -1):
            self.heapify(index)

    def max(self) -> QueueNode:
        return self.queue[1]

    def pop_max(self) -> QueueNode:
        if self.queue_size < 1:
            raise IndexError("The queue is empty")

        max = self.queue[1]
        self.queue[1] = self.queue[self.queue_size]
        self.queue_size -= 1
        self.heapify(1)

        return max

    def increase(self, index: int, new_key: int) -> None:
        if new_key < self.queue[index].key:
            raise ValueError("New key is smaller than current")

        self.queue[index] = self.nodify(new_key)
        while index > 1 and self.queue[self.iparent(index)].key < self.queue[index].key:
            self.swap(index, self.iparent(index))
            index = self.iparent(index)

    def insert(self, key: int) -> None:
        self.queue_size += 1
        self.queue[self.queue_size] = self.nodify(float("-inf"))
        self.increase(self.queue_size, key)

    def __repr__(self) -> str:
        return f"{self.queue}"


if __name__ == "__main__":
    array = [50, 20, 14, 6, 10, 45, 5, 4]

    queue = PriorityQueue()
    queue.build(array)

    print(queue)
    print(queue.max())

    print(queue.pop_max())
    print(queue)

    queue.increase(2, 100)
    print(queue)

    queue.insert(200)
    print(queue)
