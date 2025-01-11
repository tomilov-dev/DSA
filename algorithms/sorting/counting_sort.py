class CountingSort(object):
    def sort(
        self,
        array: list[int],
        value_range: range,
    ):
        offset = value_range.start
        unq_values = [0 for _ in value_range]

        for value in array:
            unq_values[value] += 1

        index = 0  # index of origin array
        pointer = 0  # pointer to unique values array
        while pointer < len(unq_values):
            if unq_values[pointer] > 0:
                array[index] = offset + pointer
                unq_values[pointer] -= 1
                index += 1
            else:
                pointer += 1


def counting_sort_with_dict(
    values: list,
) -> None:
    mapper = dict()
    for v in values:
        mapper[v] = mapper.get(v, 0) + 1

    index = 0
    keys = sorted(mapper.keys())
    for key in keys:
        count = mapper[key]
        while count > 0:
            values[index] = key
            index += 1
            count -= 1


if __name__ == "__main__":
    array = list(range(10, -1, -1))

    # sorter = CountingSort()
    # sorter.sort(array, range(0, 11))

    counting_sort_with_dict(array)
    print(array)
