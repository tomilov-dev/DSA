class Solution:
    def is_good(
        self,
        piles: list[int],
        k: int,
        h: int,
    ) -> bool:
        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + k - 1) // k
            if hours_needed > h:
                return False
        return True

    def minEatingSpeed(
        self,
        piles: list[int],
        h: int,
    ) -> int:
        low = 0
        high = max(piles)
        while high - low > 1:
            mid = low + (high - low) // 2
            if self.is_good(piles, mid, h):
                high = mid
            else:
                low = mid

        return high


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8

    piles = [30, 11, 23, 4, 20]
    h = 5

    piles = [30, 11, 23, 4, 20]
    h = 6

    print(Solution().minEatingSpeed(piles, h))
