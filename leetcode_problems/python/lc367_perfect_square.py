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


if __name__ == "__main__":
    print(Solution().isPerfectSquare(16))
    print(Solution().isPerfectSquare(14))
    print(Solution().isPerfectSquare(1))
