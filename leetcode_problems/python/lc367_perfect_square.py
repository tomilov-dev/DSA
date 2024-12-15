class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num // min(num, 2)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                hi = mid - 1
            else:
                lo = mid + 1

        return False


class Solution2:
    def is_good(
        self,
        val: int,
        target: int,
    ) -> bool:
        return val * val <= target

    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while high - low > 1:
            mid = low + (high - low) // 2
            if self.is_good(mid, num):
                low = mid
            else:
                high = mid

        return low * low == num


if __name__ == "__main__":
    print(Solution2().isPerfectSquare(16))
    print(Solution2().isPerfectSquare(14))
    print(Solution2().isPerfectSquare(1))
