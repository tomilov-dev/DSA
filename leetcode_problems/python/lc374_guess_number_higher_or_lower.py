# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guess(self, num) -> int:
        pick = 6
        if num == pick:
            return 0
        elif num < pick:
            return -1
        else:
            return 1

    def guessNumber(self, n: int) -> int:
        lo = 0
        hi = n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            res = self.guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


if __name__ == "__main__":
    n = 10
    pick = 6
    print(Solution().guessNumber(n))
