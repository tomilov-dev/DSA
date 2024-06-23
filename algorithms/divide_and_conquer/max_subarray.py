def find_max_cross_subarray(
    array: list[int],
    low: int,
    mid: int,
    high: int,
):
    ls = float("-inf")  # left-sum
    sum = 0

    for i in range(mid, low - 1, -1):
        sum = sum + array[i]
        if sum > ls:
            ls = sum
            ml = i  # max-left

    rs = float("-inf")  # right-sum
    sum = 0

    for i in range(mid + 1, high + 1):
        sum = sum + array[i]
        if sum > rs:
            rs = sum
            mr = i  # max-right

    return (ml, mr, ls + rs)


def find_max_subarray(
    array: list[int],
    low: int,
    high: int,
):
    if low == high:
        return (low, high, array[low])

    else:
        mid = low + (high - low) // 2

        ll, lh, ls = find_max_subarray(array, low, mid)
        rl, rh, rs = find_max_subarray(array, mid + 1, high)
        cl, ch, cs = find_max_cross_subarray(array, low, mid, high)

        if ls >= rs and ls >= cs:
            return ll, lh, ls
        elif rs >= ls and rs >= cs:
            return rl, rh, rs
        else:
            return cl, ch, cs


if __name__ == "__main__":
    data = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    spreads = [data[i] - data[i - 1] for i in range(1, len(data))]

    res = find_max_subarray(spreads, 0, len(spreads) - 1)
    print(res)
