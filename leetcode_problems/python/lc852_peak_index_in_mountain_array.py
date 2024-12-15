class Solution:
    def is_good(
        self,
        arr: list[int],
        i: int,
    ) -> bool:
        if i == 0:
            return True
        return arr[i] > arr[i - 1]

    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low, high = 0, len(arr) - 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if self.is_good(arr, mid):
                low = mid
            else:
                high = mid
        return low


if __name__ == "__main__":
    arr = [3, 4, 5, 1]
    print(Solution().peakIndexInMountainArray(arr))
