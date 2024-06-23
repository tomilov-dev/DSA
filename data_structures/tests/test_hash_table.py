import sys
import pytest
import random
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from hash_table import (
    ListBucket,
    ListHashMapping,
    LinkedListBucket,
    LinkedListHashMapping,
    DynamicArrayBucket,
    DynamicArrayMapping,
)


class BaseBucketTest(object):
    @pytest.fixture
    def bucket_cls(self) -> ListBucket:
        return ListBucket

    @pytest.fixture
    def test_values(self):
        return list(range(4))

    def test_put(self, bucket_cls, test_values: list[int]):
        bucket: ListBucket = bucket_cls()

        for value in test_values:
            bucket.put(value, value)

        assert list(bucket.values()) == test_values

    def test_get(self, bucket_cls, test_values: list[int]):
        bucket: ListBucket = bucket_cls()

        for value in test_values:
            bucket.put(value, value)
            putted = bucket.get(value)

            assert putted == value

    def test_remove(self, bucket_cls, test_values: list[int]):
        bucket: ListBucket = bucket_cls()

        for value in test_values:
            bucket.put(value, value)
            putted = bucket.get(value)

            assert putted == value

        for value in test_values:
            bucket.remove(value)

            assert value not in bucket

        assert len(bucket) == 0

    def test_values_iter(self, bucket_cls, test_values: list[int]):
        bucket: ListBucket = bucket_cls()

        for value in test_values:
            bucket.put(value, value)

        for value in bucket.values():
            assert value in test_values

    def test_items_iter(self, bucket_cls, test_values: list[int]):
        bucket: ListBucket = bucket_cls()

        for value in test_values:
            bucket.put(value, value)

        for k, v in bucket.items():
            assert k == v

    def test_len(self, bucket_cls, test_values: list[int]):
        bucket: ListBucket = bucket_cls()

        for value in test_values:
            bucket.put(value, value)

        assert len(bucket) == len(test_values)

    def test_contains(self, bucket_cls, test_values: list[int]):
        bucket: ListBucket = bucket_cls()

        for value in test_values:
            bucket.put(value, value)

        assert (test_values[0] in bucket) == True
        assert (999 in bucket) == False

    def test_getitem_setitem(self, bucket_cls, test_values: list[int]):
        bucket: ListBucket = bucket_cls()

        for value in test_values:
            bucket[value] = value

        for value in test_values:
            assert bucket[value] == value


class BaseHashMappingTest(BaseBucketTest):
    @pytest.fixture
    def hash_mapping_cls(self) -> ListHashMapping:
        return ListHashMapping

    @pytest.fixture
    def test_values(self):
        return list(range(4))

    def test_update(self, hash_mapping_cls):
        hash_mapping: ListHashMapping = hash_mapping_cls()

        hash_mapping.put(1, "a")
        assert hash_mapping.get(1) == "a"

        hash_mapping.put(1, "b")
        assert hash_mapping.get(1) == "b"


class TestListBucket(BaseBucketTest):
    @pytest.fixture
    def bucket_cls(self) -> ListBucket:
        return ListBucket


class TestListHashMapping(BaseBucketTest):
    @pytest.fixture
    def bucket_cls(self) -> ListHashMapping:
        return ListHashMapping


class TestLinkedListBucket(BaseBucketTest):
    @pytest.fixture
    def bucket_cls(self) -> LinkedListBucket:
        return LinkedListBucket


class TestLinkedListHashMapping(BaseBucketTest):
    @pytest.fixture
    def bucket_cls(self) -> LinkedListHashMapping:
        return LinkedListHashMapping


class TestDynamicArrayBucket(BaseBucketTest):
    @pytest.fixture
    def bucket_cls(self) -> DynamicArrayBucket:
        return DynamicArrayBucket


class TestDynamicArrayMapping(BaseBucketTest):
    @pytest.fixture
    def bucket_cls(self) -> DynamicArrayMapping:
        return DynamicArrayMapping
