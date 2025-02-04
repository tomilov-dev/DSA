class Solution:
    def shoppingOffers(
        self,
        price: list[int],
        special: list[list[int]],
        needs: list[int],
    ) -> int:
        def backtrack(
            cursum: int,
            wholesum: int,
            force_return: bool = False,
        ) -> None:
            nonlocal minsum

            if force_return:
                return None
            if cursum > minsum:
                return None

            check_sum = cursum + sum([price[i] * needs[i] for i in range(len(price))])
            minsum = min(minsum, check_sum)

            for j in range(len(special)):
                offer = special[j]
                for prod, count in enumerate(offer[:-1]):
                    needs[prod] -= count
                    if needs[prod] < 0:
                        force_return = True
                cursum += offer[-1]

                backtrack(cursum, wholesum, force_return)

                for prod, count in enumerate(offer[:-1]):
                    needs[prod] += count
                cursum -= offer[-1]
                force_return = False

        minsum = sum([price[i] * needs[i] for i in range(len(price))])
        wholesum = minsum
        backtrack(0, wholesum)
        return minsum


class SolutionMemoization:
    def shoppingOffers(
        self,
        price: list[int],
        special: list[list[int]],
        needs: list[int],
    ) -> int:
        def backtrack(needs: tuple) -> int:
            if needs in memo:
                return memo[needs]

            min_cost = sum(price[i] * needs[i] for i in range(len(price)))

            for offer in special:
                new_needs = list(needs)
                for i in range(len(price)):
                    new_needs[i] -= offer[i]
                    if new_needs[i] < 0:
                        break
                else:
                    min_cost = min(min_cost, offer[-1] + backtrack(tuple(new_needs)))

            memo[needs] = min_cost
            return min_cost

        memo = {}
        return backtrack(tuple(needs))


if __name__ == "__main__":
    price = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]

    price = [2, 3, 4]
    special = [[1, 1, 0, 4], [2, 2, 1, 9]]
    needs = [1, 2, 1]

    price = [6, 3, 6, 9, 4, 7]
    special = [[1, 2, 5, 3, 0, 4, 29], [3, 1, 3, 0, 2, 2, 19]]
    needs = [4, 1, 5, 2, 2, 4]
    print(Solution().shoppingOffers(price, special, needs))
