class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n = len(arr)
        j = n + arr.count(0)
        i = n - 1
        while i >= 0:
            j -= 1
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0

            i -= 1


if __name__ == "__main__":
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    arr = [0, 1, 7, 6, 0, 2, 0, 7]
    print(Solution().duplicateZeros(arr))
