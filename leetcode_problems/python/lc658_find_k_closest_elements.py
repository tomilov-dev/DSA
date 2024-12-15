class Solution:
    def show(
        self,
        low: int,
        high: int,
        mid: int,
    ) -> None:
        print("low:", low, "high:", high, "mid:", mid)

    def findClosestElements(
        self,
        arr: list[int],
        k: int,
        x: int,
    ) -> list[int]:
        def good(i: int):
            return x - arr[i] > arr[i + k] - x

        low = -1
        high = len(arr) - k
        while high - low > 1:
            mid = low + (high - low) // 2
            self.show(low, high, mid)
            if good(mid):
                low = mid
                print("low changed:", low)
            else:
                high = mid
                print("high changed:", high)

        return arr[high : high + k]


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 10]
    k = 5
    x = 10

    print(len(arr))
    print(Solution().findClosestElements(arr, k, x))
