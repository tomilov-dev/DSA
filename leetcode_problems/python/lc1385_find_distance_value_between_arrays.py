class Solution:
    def findTheDistanceValue(
        self,
        arr1: list[int],
        arr2: list[int],
        d: int,
    ) -> int:
        distance = 0
        for i in range(len(arr1)):
            valid = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    valid = False
                    break

            if valid:
                distance += 1

        return distance


if __name__ == "__main__":
    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d = 2

    print(Solution().findTheDistanceValue(arr1, arr2, d))
