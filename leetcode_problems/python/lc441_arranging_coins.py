class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo = 1
        hi = n
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            c = mid * (mid + 1) // 2
            if c == n:
                return mid
            elif c > n:
                hi = mid - 1
            else:
                lo = mid

        return lo


if __name__ == "__main__":
    print(Solution().arrangeCoins(5))
    print(Solution().arrangeCoins(8))
    print(Solution().arrangeCoins(10))
