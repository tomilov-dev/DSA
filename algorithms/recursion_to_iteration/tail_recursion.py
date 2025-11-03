def factorial_tail(n: int, acc: int = 1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, n * acc)


def factorial_iter(n: int):
    acc = 1
    while n > 0:
        acc *= n
        n -= 1
    return acc
