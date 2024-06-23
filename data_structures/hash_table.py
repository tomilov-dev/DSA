from abc import ABC, abstractmethod
from typing import List, Tuple

from linked_list import AdvancedDoublyLinkedList, AbstractNode
from arrays import DynamicArray


class Mapper(object):
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"{self.key} : {self.value}"

    def __hash__(self) -> int:
        return hash(self.key)


class AbstactMapping(ABC):
    @abstractmethod
    def _mapping_iter(self) -> List[Mapper]:
        pass

    @abstractmethod
    def get(self, key: int) -> int | None:
        pass

    @abstractmethod
    def put(self, key: int, value: int) -> None:
        pass

    @abstractmethod
    def remove(self, key: int) -> None:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    def values(self) -> Tuple[int]:
        return (m.value for m in self._mapping_iter())

    def items(self) -> Tuple[Tuple[int, int]]:
        return ((m.key, m.value) for m in self._mapping_iter())

    def __iter__(self) -> Tuple[int]:
        return (m.key for m in self._mapping_iter())

    def __contains__(self, key: int) -> bool:
        value = self.get(key)
        return False if value == None else True

    def __getitem__(self, key: int) -> int | None:
        return self.get(key)

    def __setitem__(self, key: int, value: int) -> None:
        self.put(key, value)

    def __str__(self) -> str:
        return "{" + ", ".join(str(m) for m in self._mapping_iter()) + "}"


class ListBucket(AbstactMapping):
    def __init__(self) -> None:
        self._storage: List[Mapper] = []

    def _mapping_iter(self) -> List[Mapper]:
        return iter(self._storage)

    def __get_mapper(self, key: int) -> Mapper | None:
        for mapper in self._storage:
            if mapper.key == key:
                return mapper
        return None

    def put(self, key: int, value: int) -> None:
        mapper = self.__get_mapper(key)
        if mapper is None:
            self._storage.append(Mapper(key, value))
        else:
            mapper.value = value

    def get(self, key: int) -> int | None:
        mapper = self.__get_mapper(key)
        value = mapper.value if mapper else None
        return value

    def remove(self, key: int) -> None:
        mapper = self.__get_mapper(key)
        self._storage.remove(mapper)

    def __len__(self) -> int:
        return len(self._storage)


class ListHashMapping(AbstactMapping):
    def __init__(self, size: int = 2) -> None:
        self._length = 0
        self._size = size

        self._buckets = [ListBucket() for _ in range(self._size)]

    def __get_bucket(self, key: int) -> ListBucket:
        return self._buckets[hash(key) % self._size]

    def _mapping_iter(self) -> List[Mapper]:
        return (m for b in self._buckets for m in b._mapping_iter())

    def _add_buckets(self) -> None:
        if self._length > self._size:
            self._size *= 2

            old_buckets = self._buckets
            self._buckets = [ListBucket() for _ in range(self._size)]

            for bucket in old_buckets:
                for key, value in bucket.items():
                    new_bucket = self.__get_bucket(key)
                    new_bucket[key] = value

    def put(self, key: int, value: int) -> None:
        bucket = self.__get_bucket(key)
        if key not in bucket:
            self._length += 1
        bucket[key] = value

        self._add_buckets()

    def get(self, key: int) -> int:
        bucket = self.__get_bucket(key)
        return bucket[key]

    def remove(self, key: int) -> None:
        bucket = self.__get_bucket(key)
        bucket.remove(key)
        self._length -= 1

    def __len__(self) -> int:
        return self._length


class LinkedListBucket(AbstactMapping):
    def __init__(self) -> None:
        self._storage: AdvancedDoublyLinkedList[Mapper] = AdvancedDoublyLinkedList()

    def _mapping_iter(self) -> List[Mapper]:
        return iter(self._storage)

    def __get_mapper(self, key: int) -> Mapper | None:
        for node in self._storage:
            node: AbstractNode

            mapper: Mapper = node.value
            if mapper.key == key:
                return mapper

        return None

    def put(self, key: int, value: int) -> None:
        mapper = self.__get_mapper(key)
        if mapper is None:
            self._storage.append(Mapper(key, value))
        else:
            mapper.value = value

    def get(self, key: int) -> int | None:
        mapper = self.__get_mapper(key)
        value = mapper.value if mapper else None
        return value

    def remove(self, key: int) -> None:
        mapper = self.__get_mapper(key)
        self._storage.remove_value(mapper)

    def values(self) -> Tuple[int]:
        return (m.value.value for m in self._mapping_iter())

    def items(self) -> Tuple[Tuple[int, int]]:
        return ((m.value.key, m.value.value) for m in self._mapping_iter())

    def __len__(self) -> int:
        return len(self._storage)


class LinkedListHashMapping(AbstactMapping):
    def __init__(self, size: int = 2) -> None:
        self._length = 0
        self._size = size

        self._buckets = [LinkedListBucket() for _ in range(self._size)]

    def __get_bucket(self, key: int) -> LinkedListBucket:
        return self._buckets[hash(key) % self._size]

    def _mapping_iter(self) -> List[Mapper]:
        return (m for b in self._buckets for m in b._mapping_iter())

    def _add_buckets(self) -> None:
        if self._length > self._size:
            self._size *= 2

            old_buckets = self._buckets
            self._buckets = [LinkedListBucket() for _ in range(self._size)]

            for bucket in old_buckets:
                for key, value in bucket.items():
                    new_bucket = self.__get_bucket(key)
                    new_bucket[key] = value

    def put(self, key: int, value: int) -> None:
        bucket = self.__get_bucket(key)
        if key not in bucket:
            self._length += 1
        bucket[key] = value

        self._add_buckets()

    def get(self, key: int) -> int:
        bucket = self.__get_bucket(key)
        return bucket[key]

    def remove(self, key: int) -> None:
        bucket = self.__get_bucket(key)
        bucket.remove(key)
        self._length -= 1

    def values(self) -> Tuple[int]:
        return (m.value.value for m in self._mapping_iter())

    def items(self) -> Tuple[Tuple[int, int]]:
        return ((m.value.key, m.value.value) for m in self._mapping_iter())

    def __len__(self) -> int:
        return self._length


class DynamicArrayBucket(AbstactMapping):
    def __init__(self) -> None:
        self._storage: DynamicArray[Mapper] = DynamicArray()

    def _mapping_iter(self) -> List[Mapper]:
        return iter(self._storage)

    def __get_mapper(self, key: int) -> Mapper | None:
        for mapper in self._storage:
            if mapper.key == key:
                return mapper
        return None

    def put(self, key: int, value: int) -> None:
        mapper = self.__get_mapper(key)
        if mapper is None:
            self._storage.append(Mapper(key, value))
        else:
            mapper.value = value

    def get(self, key: int) -> int | None:
        mapper = self.__get_mapper(key)
        value = mapper.value if mapper else None
        return value

    def remove(self, key: int) -> None:
        mapper = self.__get_mapper(key)
        self._storage.remove_value(mapper)

    def __len__(self) -> int:
        return len(self._storage)


class DynamicArrayMapping(AbstactMapping):
    def __init__(self, size: int = 2) -> None:
        self._length = 0
        self._size = size

        self._buckets = [DynamicArrayBucket() for _ in range(self._size)]

    def __get_bucket(self, key: int) -> DynamicArrayBucket:
        return self._buckets[hash(key) % self._size]

    def _mapping_iter(self) -> List[Mapper]:
        return (m for b in self._buckets for m in b._mapping_iter())

    def _add_buckets(self) -> None:
        if self._length > self._size:
            self._size *= 2

            old_buckets = self._buckets
            self._buckets = [DynamicArrayBucket() for _ in range(self._size)]

            for bucket in old_buckets:
                for key, value in bucket.items():
                    new_bucket = self.__get_bucket(key)
                    new_bucket[key] = value

    def put(self, key: int, value: int) -> None:
        bucket = self.__get_bucket(key)
        if key not in bucket:
            self._length += 1
        bucket[key] = value

        self._add_buckets()

    def get(self, key: int) -> int:
        bucket = self.__get_bucket(key)
        return bucket[key]

    def remove(self, key: int) -> None:
        bucket = self.__get_bucket(key)
        bucket.remove(key)
        self._length -= 1

    def __len__(self) -> int:
        return self._length


def ListBucket_fast_test():
    bucket = ListBucket()

    bucket.put(1, 10)
    bucket.put(2, 20)
    bucket.put(3, 30)

    for key, value in bucket.items():
        print(key, value)


def ListHashMapping_fast_test():
    hashmap = ListHashMapping()

    hashmap.put(1, 10)
    hashmap.put(2, 20)
    hashmap.put(3, 30)

    for key, value in hashmap.items():
        print(key, value)

    hashmap.put(1, "a")
    print(hashmap.get(1))
    hashmap.put(1, "b")
    print(hashmap.get(1))


def LinkedListBucket_fast_test():
    bucket = LinkedListBucket()

    bucket.put(1, 10)
    bucket.put(2, 20)
    bucket.put(3, 30)

    for key, value in bucket.items():
        print(key, value)


def LinkedListHashMapping_fast_test():
    hashmap = ListHashMapping()

    hashmap.put(1, 10)
    hashmap.put(2, 20)
    hashmap.put(3, 30)

    for key, value in hashmap.items():
        print(key, value)


def DynamicArrayBucket_fast_test():
    bucket = DynamicArrayBucket()

    bucket.put(1, 10)
    bucket.put(2, 20)
    bucket.put(3, 30)

    for key, value in bucket.items():
        print(key, value)


def DynamicArrayMapping_fast_test():
    hashmap = DynamicArrayMapping()

    hashmap.put(1, 10)
    hashmap.put(2, 20)
    hashmap.put(3, 30)

    for key, value in hashmap.items():
        print(key, value)


if __name__ == "__main__":
    ListHashMapping_fast_test()
