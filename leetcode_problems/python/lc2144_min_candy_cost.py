class Solution:
    def minimumCost(
        self,
        cost: list[int],
    ) -> int:
        cost.sort(reverse=True)

        index = 0
        total_cost = 0
        while index < len(cost):
            if index + 2 < len(cost):
                total_cost += cost[index] + cost[index + 1]
                index += 3
            else:
                total_cost += cost[index]
                index += 1

        return total_cost


if __name__ == "__main__":
    cost = [6, 5, 7, 9, 2, 2]
    # cost = [1, 2, 3]

    print(Solution().minimumCost(cost))
