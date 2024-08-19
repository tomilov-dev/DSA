class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        sumof = sum(arr)
        trisum = sumof / 3

        iters = 0
        cursum = 0
        for index in range(len(arr)):
            num = arr[index]
            cursum += num

            if iters < 2:
                if cursum == trisum:
                    cursum = 0
                    iters += 1
            else:
                if cursum == trisum:
                    iters += 1

        return cursum == trisum and iters >= 3


if __name__ == "__main__":
    arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]

    arr = [18, 12, -18, 18, -19, -1, 10, 10]

    arr = [1, -1, 1, -1]

    print(Solution().canThreePartsEqualSum(arr))
