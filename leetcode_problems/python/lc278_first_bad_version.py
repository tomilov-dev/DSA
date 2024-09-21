# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1

        return hi


def isBadVersion(version: int):
    if version >= bad:
        return True
    return False


if __name__ == "__main__":
    n = 5
    bad = 4

    print(Solution().firstBadVersion(n))
