def bsearch(
    array: list[int],
    target: int,
    left: int,
    right: int,
) -> int | None:
    if left == right:
        if array[left] == target:
            return left
        return None

    else:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return bsearch(array, target, left, mid)
        else:
            return bsearch(array, target, mid + 1, right)


if __name__ == "__main__":
    data = [1, 3, 4, 6, 7, 9, 14]
    target_ind = 5

    res = bsearch(data, data[target_ind], 0, len(data) - 1)
    print(res)
