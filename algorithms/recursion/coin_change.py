class SolutionRecursive:
    def count(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        def change(sum: int, c: int) -> int:
            if sum == 0:
                return c
            if sum < 0:
                return 10**5

            mini = 10**5
            for coin in coins:
                mini = min(mini, change(sum - coin, c + 1))
            return mini

        return change(sum, 0)


class SolutionTopDown:
    def count(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        def change(sum: int, c: int) -> int:
            if sum == 0:
                return c
            if sum < 0:
                return MAX

            key = (sum, c)
            if key not in mem:
                mem[key] = MAX
                for coin in coins:
                    mem[key] = min(mem[key], change(sum - coin, c + 1))
            return mem[key]

        mem = {}
        MAX = 10**5
        res = change(sum, 0)
        return -1 if res == MAX else res


if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 4

    coins = [2, 5, 3, 6]
    sum = 10
    print(SolutionRecursive().count(coins, sum))
    print(SolutionTopDown().count(coins, sum))
