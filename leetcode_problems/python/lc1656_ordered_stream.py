class OrderedStream:

    def __init__(self, n: int):
        self._storage = [None] * n
        self._ptr = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self._storage[idKey - 1] = value

        chunk = []
        for index in range(self._ptr, len(self._storage)):
            data = self._storage[index]
            if data is None:
                break

            chunk.append(data)
            self._ptr += 1

        return chunk


if __name__ == "__main__":
    stream = OrderedStream(5)

    data = [[3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]

    stream.insert(*data[0])
    stream.insert(*data[1])
    stream.insert(*data[2])
