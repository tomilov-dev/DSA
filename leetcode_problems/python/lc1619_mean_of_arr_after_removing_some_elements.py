class Solution:
    def mean(self, arr: list[int]) -> float:
        return sum(arr) / len(arr)

    def trimMean(self, arr: list[int]) -> float:
        arr_sorted = sorted(arr)
        limit = int(0.05 * len(arr_sorted))
        return self.mean(arr_sorted[limit : len(arr_sorted) - limit])


if __name__ == "__main__":
    arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]
    print(Solution().trimMean(arr))
