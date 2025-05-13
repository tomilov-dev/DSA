class SolutionRecursive:
    def count(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        def rec(i: int, sum: int) -> int:
            if sum == 0:
                return 1
            if sum < 0 or i >= len(coins):
                return 0
            return rec(i, sum - coins[i]) + rec(i + 1, sum)

        return rec(0, sum)


class SolutionTopDown:
    def count(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        def rec(i: int, sum: int) -> int:
            if sum == 0:
                return 1
            if sum < 0 or i >= len(coins):
                return 0
            key = (i, sum)
            if key not in mem:
                mem[key] = rec(i, sum - coins[i]) + rec(i + 1, sum)
            return mem[key]

        mem = {}
        return rec(0, sum)


if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 4

    # coins = [2, 5, 3, 6]
    # sum = 10
    print(SolutionRecursive().count(coins, sum))
    print(SolutionTopDown().count(coins, sum))
