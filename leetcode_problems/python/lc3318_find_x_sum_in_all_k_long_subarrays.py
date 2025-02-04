class Solution:
    def findXSum(
        self,
        nums: list[int],
        k: int,
        x: int,
    ) -> list[int]:
        def count(mapper: dict[int, int]) -> int:
            arr = [(fq, num) for num, fq in mapper.items()]
            if len(mapper) < x:
                return sum([fq * num for fq, num in arr])

            arr.sort(reverse=True)
            return sum([fq * num for fq, num in arr[:x]])

        mapx = dict()

        for num in nums[:k]:
            mapx[num] = mapx.get(num, 0) + 1
        res = [count(mapx)]

        for i in range(len(nums) - k + 1):
            if i == 0:
                continue

            prev = nums[i - 1]
            cur = nums[i + k - 1]
            mapx[prev] = mapx.get(prev, 0) - 1
            if mapx[prev] <= 0:
                del mapx[prev]
            mapx[cur] = mapx.get(cur, 0) + 1

            res.append(count(mapx))

        return res


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 2, 3]
    k = 6
    x = 2
    print(Solution().findXSum(nums, k, x))
