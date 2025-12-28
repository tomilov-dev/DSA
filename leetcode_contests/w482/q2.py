class Solution:
    def minimumCost(
        self,
        cost1: int,
        cost2: int,
        costBoth: int,
        need1: int,
        need2: int,
    ) -> int:
        total = 0
        if costBoth <= cost1 and costBoth <= cost2:
            return costBoth * max(need1, need2)
        if costBoth <= cost1 + cost2:
            x = min(need1, need2)
            total += x * costBoth
            need1 -= x
            need2 -= x
        if costBoth <= cost1:
            x = need1
            total += x * costBoth
            need1 -= x
            need2 -= x
        if costBoth <= cost2:
            x = need2
            total += x * costBoth
            need1 -= x
            need2 -= x

        total += need1 * cost1
        total += need2 * cost2
        return total


class Solution:
    def minimumCost(
        self,
        cost1: int,
        cost2: int,
        costBoth: int,
        need1: int,
        need2: int,
    ) -> int:
        mini = float("inf")
        maxb = max(need1, need2) + 1
        for both in range(maxb):
            c1 = max(0, need1 - both)
            c2 = max(0, need2 - both)
            cur = both * costBoth + c1 * cost1 + c2 * cost2
            mini = min(mini, cur)
        return mini


class Solution:
    def minimumCost(
        self,
        cost1: int,
        cost2: int,
        costBoth: int,
        need1: int,
        need2: int,
    ) -> int:
        def cost(both: int) -> int:
            c1 = max(0, need1 - both)
            c2 = max(0, need2 - both)
            return both * costBoth + c1 * cost1 + c2 * cost2

        l = 0
        h = max(need1, need2)
        while h - l > 3:
            m1 = l + (h - l) // 3
            m2 = h - (h - l) // 3
            if cost(m1) < cost(m2):
                h = m2
            else:
                l = m1
        mini = float("inf")
        for both in range(l, h + 1):
            mini = min(mini, cost(both))
        return mini


if __name__ == "__main__":
    cost1 = 3
    cost2 = 2
    costBoth = 1
    need1 = 3
    need2 = 2

    cost1 = 5
    cost2 = 4
    costBoth = 15
    need1 = 2
    need2 = 3

    cost1 = 5
    cost2 = 4
    costBoth = 15
    need1 = 0
    need2 = 0

    cost1 = 50
    cost2 = 55
    costBoth = 72
    need1 = 5
    need2 = 3

    cost1 = 37
    cost2 = 53
    costBoth = 45
    need1 = 5
    need2 = 18
    print(Solution().minimumCost(cost1, cost2, costBoth, need1, need2))
