import random


def partition(
    array: list[int],
    start: int,
    end: int,
) -> int:
    x = array[end]

    i = start - 1
    for j in range(start, end):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1
    array[i], array[end] = array[end], array[i]
    return i


def reverse_partition(
    array: list[int],
    start: int,
    end: int,
) -> int:
    x = array[end]

    i = start - 1
    for j in range(start, end):
        if array[j] >= x:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1
    array[i], array[end] = array[end], array[i]
    return i


def quickselect(
    array: list[int],
    start: int,
    end: int,
    k: int,
) -> list[int]:
    if start > end:
        return

    q = reverse_partition(array, start, end)
    if q == k - 1:
        return array[: q + 1]
    elif q < k - 1:
        return quickselect(array, q + 1, end, k)
    else:
        return quickselect(array, start, q - 1, k)


def pyquickselect(
    array: list[int],
    k: int,
) -> int:
    if not array:
        return

    x = random.choice(array)
    left = [v for v in array if v < x]
    mid = [v for v in array if v == x]
    right = [v for v in array if v > x]

    if k <= len(right):
        return pyquickselect(right, k)
    elif k > len(mid) + len(right):
        return pyquickselect(left, k - len(right) - len(mid))
    else:
        return mid[0]


if __name__ == "__main__":
    array = [10, 4, 5, 8, 6, 11, 26]
    k = 3

    # klarge = quickselect(array, 0, len(array) - 1, 3)
    # print(klarge)

    print(pyquickselect(array, k))
