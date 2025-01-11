class Solution:
    def is_good(
        self,
        weights: list[int],
        ship: int,
        days: int,
    ) -> bool:
        curw = 0
        curd = 1
        for w in weights:
            if curw + w > ship:
                curd += 1
                curw = w
            else:
                curw += w

            if curd > days:
                return False
        return True

    def shipWithinDays(
        self,
        weights: list[int],
        days: int,
    ) -> int:
        low = max(weights) - 1
        high = sum(weights)
        while high - low > 1:
            mid = low + (high - low) // 2
            if self.is_good(weights, mid, days):
                high = mid
            else:
                low = mid

        return high


if __name__ == "__main__":
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5

    weights = [3, 2, 2, 4, 1, 4]
    days = 3

    weights = [1, 2, 3, 1, 1]
    days = 4

    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 10

    print(Solution().shipWithinDays(weights, days))
