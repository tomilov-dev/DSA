def greedy(coins: list[int], change: int) -> int:
    coins.reverse()

    count = 0
    for coin in coins:
        count += change // coin
        change = change % coin

    return count


def recursive(coins: list[int], change: int) -> int:
    min_coins = change
    if change in coins:
        return 1
    else:
        for ncoin in [coin for coin in coins if coin <= change]:
            num_coins = 1 + recursive(coins, change - ncoin)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


def memoize(
    coins: list[int],
    change: int,
    memo: dict[int, int] = {},
) -> int:
    min_coins = change
    if change in coins:
        return 1
    elif change in memo:
        return memo[change]
    else:
        for ncoin in [coin for coin in coins if coin <= change]:
            num_coins = 1 + memoize(coins, change - ncoin, memo)
            if num_coins < min_coins:
                min_coins = num_coins
                memo[change] = min_coins

    return min_coins


def dp(
    coins: list[int],
    change: int,
):
    min_coins = [None] * (change + 1)

    for cents in range(change + 1):
        min_coins[cents] = cents
        for coin in coins:
            if cents >= coin:
                min_coins[cents] = min(min_coins[cents], min_coins[cents - coin] + 1)

    return min_coins[change]


class Testcase(object):
    def __init__(
        self,
        id: int,
        inputs: tuple[list[int], int],
        answer: int,
    ) -> None:
        self.id = id
        self.inputs = inputs
        self.answer = answer

    def __repr__(self) -> str:
        return str(self.id)


def run_testcases(solution: callable) -> bool:
    testcases = [
        Testcase(1, ([1, 5, 10, 25], 63), 6),
        Testcase(2, ([1, 21, 25], 63), 3),
        Testcase(3, ([1, 5, 21, 25], 63), 3),
    ]

    for testcase in testcases:
        output = solution(*testcase.inputs)
        assert output == testcase.answer, print(testcase, output, testcase.answer)

    return True


if __name__ == "__main__":
    # run_testcases(greedy)
    # run_testcases(recursive)
    # run_testcases(memoize)
    run_testcases(dp)
