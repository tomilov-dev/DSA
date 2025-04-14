class Solution:
    def closestCost(
        self,
        baseCosts: list[int],
        toppingCosts: list[int],
        target: int,
    ) -> int:
        def get_min(total: int) -> int:
            sp1 = target - total
            sp2 = target - mini
            if total == target:
                return target
            elif abs(sp1) > abs(sp2):
                return mini
            elif abs(sp1) < abs(sp2):
                return total
            else:
                return total if sp1 > sp2 else mini

        def backtrack(i: int):
            nonlocal mini
            nonlocal total

            if total >= target:
                mini = get_min(total)
                return None
            if i == len(toppingCosts):
                mini = get_min(total)
                return None

            backtrack(i + 1)
            total += toppingCosts[i]
            backtrack(i + 1)
            total += toppingCosts[i]
            backtrack(i + 1)
            total -= 2 * toppingCosts[i]

        mini = 10**6
        total = 0
        for bc in baseCosts:
            total += bc
            backtrack(0)
            total -= bc
        return mini


if __name__ == "__main__":
    baseCosts = [1, 7]
    toppingCosts = [3, 4]
    target = 10

    baseCosts = [2, 3]
    toppingCosts = [4, 5, 100]
    target = 18

    baseCosts = [4]
    toppingCosts = [9]
    target = 9

    print(Solution().closestCost(baseCosts, toppingCosts, target))
