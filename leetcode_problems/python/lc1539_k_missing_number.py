class Solution:
    def findKthPositive(
        self,
        arr: list[int],
        k: int,
    ) -> int:
        lo = 0
        hi = len(arr)
        while lo < hi:
            m = lo + (hi - lo) // 2
            if arr[m] - 1 - m < k:
                lo = m + 1
            else:
                hi = m
        return lo + k


if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(Solution().findKthPositive(arr, k))
