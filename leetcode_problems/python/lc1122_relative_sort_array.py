class Solution:
    def relativeSortArray(
        self,
        arr1: list[int],
        arr2: list[int],
    ) -> list[int]:
        map1 = dict()
        for num in arr1:
            map1[num] = map1.get(num, 0) + 1

        arr = []
        for num in arr2:
            subarr = [num] * map1.get(num, 0)
            map1[num] = 0
            arr.extend(subarr)

        subarr = []
        for num, freq in map1.items():
            if freq > 0:
                resarr = [num] * freq
                subarr.extend(resarr)

        arr.extend(sorted(subarr))

        return arr


if __name__ == "__main__":
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(Solution().relativeSortArray(arr1, arr2))
